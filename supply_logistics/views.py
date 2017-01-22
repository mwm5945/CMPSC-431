from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DeleteView, DetailView, FormView, TemplateView, UpdateView

from rest_framework.reverse import reverse_lazy

from . import forms
from . import models


class SupplyLogisticsView(TemplateView):
    """Class based view to handle supply logistics landing page."""

    template_name = 'supply_logistics/supply_logistics.html'


class MerchInventoryLandingView(TemplateView):
    """Class based view for the Merchandise Inventory Home."""

    template_name = "supply_logistics/merch_inventory_landing.html"


class MerchInventoryAddItemView(FormView):
    """Class based view for adding an item to inventory."""

    template_name = "supply_logistics/merch_inventory_add_item.html"
    form_class = forms.MerchInventoryAddItemForm

    def form_valid(self, form):
        """Method for handing valid form POST."""
        new_item = form.save(commit=False)
        new_item.user = self.request.user
        total = (new_item.item_quantity1 + new_item.item_quantity2 + new_item.item_quantity3 + new_item.item_quantity1 +
                 new_item.item_quantity5)
        new_item.total_on_hand = total
        new_item.save()
        messages.success(self.request, """Item Added Successfully: %s""" % new_item.item_name)

        return render(self.request, self.template_name, {'form': form})

    def form_invalid(self, form):
        """"Method for handling invalid form information."""
        messages.warning(self.request, 'You have errors in your submission. Please fix them before continuing.')
        form = forms.MerchInventoryAddItemForm(self.request.POST)
        return render(self.request, self.template_name, {'form': form})


class MerchInventoryDeleteItemView(DeleteView):
    """Class based view for deleting items from inventory."""

    model = models.MerchandiseInventoryItem
    template_name = 'supply_logistics/supply_logistics_confirm_delete.html'

    def get_success_url(self):
        """Get the success URL."""
        messages.success(self.request, 'Inventory item  removed successfully.')

        return reverse_lazy('supply_logistics:registry-admin-home')


class MerchInventoryItemUpdateView(UpdateView):
    """Class based view for the updating an item already in inventory."""

    model = models.MerchandiseInventoryItem
    form_class = forms.MerchInventoryAddItemForm
    template_name = 'supply_logistics/merch_inventory_add_item.html'

    def get(self, request, *args, **kwargs):
        """Handle the get request."""
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def form_invalid(self, form_class):
        """Handle an invalid form."""
        messages.warning(self.request, 'You have errors in your submission. Please fix them before continuing.')
        form = forms.MerchInventoryAddItemForm(self.request.POST)
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        """Return success url."""
        messages.success(self.request, 'You have successfully updated the item.')
        return reverse_lazy('supply_logistics:merch-inventory-item-detail', kwargs={'pk': self.object.id})


class MerchInventoryItemDetailView(DetailView):
    """Class based view for the item detail view."""

    model = models.MerchandiseInventoryItem
    template_name = 'supply_logistics/merch_inventory_item_detail.html'

    def get_context_data(self, **kwargs):
        """Handle the GET request."""
        context = super(MerchInventoryItemDetailView, self).get_context_data(**kwargs)
        return context


class MerchInventoryMoveItemView(FormView):
    """Class based view for moving items between locations."""


class MerchInventoryOverallStatus(DetailView):
    """Class based view for the overall inventory status."""


class MerchInventoryLocationStatus(DetailView):
    """Class based view for the inventory status at a given location."""


class MerchInventoryChangePriceView(UpdateView):
    """Class based view for updating an item price already in inventory."""
