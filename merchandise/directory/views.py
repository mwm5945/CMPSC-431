from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, FormView, UpdateView
from django_tables2 import SingleTableView

from django.shortcuts import HttpResponseRedirect, render

from .forms import SupplierSubmissionForm

# Create your views here.


class SupplierSubmissionView(FormView):
    """View to add a new supplier."""

    template_name = 'directory/supplier_submission.html'
    form_class = SupplierSubmissionForm

    def form_valid(self, form):
        """Handle the instance where the form is valid."""
        new_supplier = form.save(commit=False)
        new_supplier.save()
        messages.success(self.request, """Successfully added a new supplier!""")

        return HttpResponseRedirect(reverse('directory:'))


class SupplierDetailView(DetailView):
    """View to view supplier information."""



class SupplierListView(SingleTableView):
    """View for all suppliers."""



class SupplierUpdateView(UpdateView):
    """View to update a supplier."""

