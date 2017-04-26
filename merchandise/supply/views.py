from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from supply.models import Order

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class OrderListView(ListView):
    """List view for orders."""

    model = Order
    params = {
        'page_header': "Orders"
    }

    def get_queryset(self):
        qs = super(OrderListView, self).get_queryset()
        return qs.order_by('-timestamp')

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


class OrderCreateView(CreateView):
    """Create View for Order."""

    model = Order
    fields = ['status', 'supplier']
    params = {
        'page_header': "New Order"
    }

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form
    
    def get_success_url(self):
        return reverse('supply:order_detail', kwargs={'pk':self.object.id})


class OrderUpdateView(UpdateView):
    """Update View for Order."""

    model = Order
    fields = ['supplier', 'status']
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object
        context = super(OrderUpdateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form
    
    def get_success_url(self):
        return reverse('supply:order_detail', kwargs={'pk':self.object.id})