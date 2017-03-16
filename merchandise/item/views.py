from django.shortcuts import render
from django.views.generic import ListView, DetailView
from item.models import ItemDetails


class ItemDetailsListView(ListView):
    """List View for ItemDetails."""

    model = ItemDetails
    params = {
        'page_header': "Items"
    }

    def get_context_data(self, **kwargs):
        context = super(ItemDetailsListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class ItemDetailsDetailView(DetailView):
    """Detail View for ItemDetails."""

    model = ItemDetails
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.name
        context = super(ItemDetailsDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context
