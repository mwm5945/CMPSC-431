from django.shortcuts import render
from django.views.generic import ListView, DetailView
from supply.models import Order

class OrderListView(ListView):
    """List view for orders."""

    model = Order
    params = {
        'page_header': "Orders"
    }

    # Returns dictionary representing dictionary context... wut
    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

class OrderDetailView(DetailView):
    """Detail view for orders."""

    model = Order
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.supplier
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context