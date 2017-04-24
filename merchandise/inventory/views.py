from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from inventory.models import Inventory, InventoryTransaction


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


class CreateInventoryTransaction(CreateView):
    """Create view for inventory transaction."""

    model = InventoryTransaction
    fields = ['inventory', 'quantity']
    params = {
        'page_header': "Move Inventory"
    }

    def get_context_data(self, **kwargs):
        context = super(CreateInventoryTransaction, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form

    def get_success_url(self):
        return reverse('inventory:inventory_list')


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