from django.contrib import messages

from django.urls import reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView

from .models import Location
from .forms import LocationForm


class LocationListView(ListView):
    """View for showing all locations. Each will link to inventory page."""

    model = Location
    params = {
        'page_header': "Locations"
    }

    def get_context_data(self, **kwargs):
        context = super(LocationListView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_queryset(self):
        return super(LocationListView, self).get_queryset()


class LocationDetailView(DetailView):
    """Detail View for Location."""

    model = Location
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.name
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class LocationCreateView(CreateView):
    """Create View for Location."""

    model = Location
    form_class = LocationForm
    params = {
        'page_header': "Add Location"
    }

    def get_context_data(self, **kwargs):
        context = super(LocationCreateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_success_url(self):
        return reverse('location:location_detail', kwargs={'pk':self.object.id})


class LocationUpdateView(UpdateView):
    """Update View for Location."""

    model = Location
    form_class = LocationForm
    params = {}

    def get_context_data(self, **kwargs):
        self.params['page_header'] = self.object.name
        context = super(LocationUpdateView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

    def get_success_url(self):
        return reverse('location:location_detail', kwargs={'pk':self.object.id})