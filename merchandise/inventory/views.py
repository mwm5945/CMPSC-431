from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, FormView

from .models import Inventory, InventoryTransaction
from .forms import CreateInventoryTransactionForm

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

class UpdateInventory(UpdateView):
    """Update an inventory object."""

    model = Inventory
    fields = ['item', 'quantity', 'location']
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.item.name
        context = super(UpdateInventory, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse('inventory:inventory_list')


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
    #success_url = reverse_lazy('inventory:list_moves')

    params = {
        'page_header': "Move Inventory"
    }

    def form_valid(self, form):
        """Handle the valid form."""
        item = form.cleaned_data['inventory']
        quantity = form.cleaned_data['quantity']
        to_loc = form.cleaned_data['to_loc']
        from_loc = form.cleaned_data['from_loc']

        InventoryTransaction.move_inventory(item, from_loc, to_loc, quantity, user=self.request.user)

        return HttpResponseRedirect(reverse_lazy('inventory:list_moves'))

class ListInventoryTransactions(ListView):
    """List view for all inventory transactions."""
    model = InventoryTransaction
    params = {
        'page_header': "Inventory Movements"
    }

    def get_context_data(self, **kwargs):
        context = super(ListInventoryTransactions, self).get_context_data(**kwargs)
        context.update(self.params)
        return context