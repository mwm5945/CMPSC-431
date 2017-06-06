from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, FormView, View

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from datetime import datetime, timedelta

from .models import Inventory, InventoryTransaction
from .forms import CreateInventoryTransactionForm, UpdateInventoryForm
from sale.models import Transaction, Sale
from item.models import Item


class CreateInventory(CreateView):
    """Create an Inventory object."""

    model = Inventory
    fields = ['item', 'quantity', 'location']
    params = {
        'page_header': "Create Inventory"
    }

    def get_context_data(self, **kwargs):
        context = super(CreateInventory, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse('inventory:inventory_list')


class UpdateInventory(FormView):
    """Update an inventory object."""

    template_name = "inventory/inventory_update.html"
    form_class = UpdateInventoryForm

    def get_initial(self):
        """Get the initial data for the form."""
        inventory = Inventory.objects.get(pk=self.kwargs['pk'])
        initial = {
            'quantity': inventory.quantity,
        }
        return initial

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super(UpdateInventory, self).get_context_data(**kwargs)
        inventory = Inventory.objects.get(pk=self.kwargs['pk'])
        context.update(
            {'page_header': "Update an Inventory Item", 'item': inventory.item, 'location': inventory.location})
        return context

    def form_valid(self, form):
        """Handle a valid update."""
        new_quantity = form.cleaned_data['quantity']
        inventory = Inventory.objects.get(pk=self.kwargs['pk'])
        old_quantity = inventory.quantity

        diff = old_quantity - new_quantity

        if diff >= 0:
            InventoryTransaction.remove_from_inventory(inventory.item, inventory.location, diff, self.request.user)
        else:
            InventoryTransaction.add_to_inventory(inventory.item, inventory.location, -diff, self.request.user)

        return HttpResponseRedirect(reverse_lazy('inventory:inventory_list'))


class ListInventory(ListView):
    """List all inventory objects."""

    model = Inventory
    params = {
        'page_header': "Inventory"
    }

    def get_context_data(self, **kwargs):
        context = super(ListInventory, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class CreateInventoryTransaction(FormView):
    """Create view for inventory transaction."""

    template_name = 'inventory/inventorytransaction_form.html'
    form_class = CreateInventoryTransactionForm
    model = InventoryTransaction
    # success_url = reverse_lazy('inventory:list_moves')

    params = {
        'page_header': "Move Inventory"
    }

    def get_context_data(self, **kwargs):
        context = super(CreateInventoryTransaction, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def form_valid(self, form):
        """Handle the valid form."""
        item = form.cleaned_data['item']
        quantity = form.cleaned_data['quantity']
        to_loc = form.cleaned_data['to_location']
        from_loc = form.cleaned_data['from_location']

        InventoryTransaction.move_inventory(item, from_loc, to_loc, quantity, user=self.request.user)

        return HttpResponseRedirect(reverse_lazy('inventory:list_moves'))


class ListInventoryTransactions(ListView):
    """List view for all inventory transactions."""
    model = InventoryTransaction
    params = {
        'page_header': "Inventory Movements"
    }

    def get_queryset(self):
        qs = super(ListInventoryTransactions, self).get_queryset()
        return qs.order_by('-timestamp')

    def get_context_data(self, **kwargs):
        context = super(ListInventoryTransactions, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class InventoryReport(View):
    """View for the inventory report."""
    params = {
        'page_header': "Inventory & Sale Report"
    }

    def get(self, request, *args, **kwargs):
        # Get transactions in the past week
        one_week_ago = datetime.now() - timedelta(days=7)
        transactions = Transaction.objects.filter(timestamp__gt=one_week_ago)
        sales = Sale.objects.filter(transaction__timestamp__gt=one_week_ago)

        self.params['transactions'] = transactions
        self.params['total'] = int(sales.aggregate(models.Sum('price'))['price__sum'])

        # Get a list of the top items
        top_is = sales.values_list('item').annotate(item_count=models.Count('item')).order_by('-item_count')
        top_items = []
        for ti in top_is:
            top_items.append([Item.objects.get(id=ti[0]), ti[1]])
        self.params['top_items'] = top_items

        # Lowest Inventories
        lowest = Inventory.objects.values_list('item').annotate(in_inventory=models.Sum('quantity')).order_by('in_inventory')
        lowest_items = []
        for li in lowest:
            lowest_items.append([Item.objects.get(id=li[0]), li[1]])
        self.params['lowest_items'] = lowest_items
        
        
        return render(request, "inventory/inventory_report.html", self.params)