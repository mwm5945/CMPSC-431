from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from inventory.models import Inventory


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


    # TODO: Fix with real URL
    def get_success_url(self):
        return reverse('item:item_details_detail', kwargs={'pk':self.object.id})

class UpdateInventory(UpdateView):
    """Update an inventory object."""


class ListInventory(ListView):
    """List all inventory objects."""


class CreateInventoryTransaction(CreateView):
    """Create view for inventory transaction."""


class ListInventoryTransactions(ListView):
    """List view for all inventory transactions."""
