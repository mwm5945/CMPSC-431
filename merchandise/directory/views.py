from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from directory.models import Customer


class CustomerListView(ListView):
    """List View for Customers."""

    model = Customer
    params = {
        'page_header': "Customers"
    }

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class CustomerDetailView(DetailView):
    """Detail View for Customers."""

    model = Customer
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.email
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class CustomerUpdateView(UpdateView):
    """Update View for Customer."""

    model = Customer
    fields = ['address']
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.email
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        return form
    
    def get_success_url(self):
        return reverse('directory:customer_detail', kwargs={'pk':self.object.id})