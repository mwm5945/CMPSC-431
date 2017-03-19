from django.contrib import messages

from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from .models import Location
from .forms import CreateLocationForm


class CreateLocationView(CreateView):
    """Create View for adding a location."""

    model = Location
    form_class = CreateLocationForm
    template_name = 'location/create_location.html'
    success_url = reverse_lazy('location:list_locations')


class ListLocationView(ListView):
    """View for showing all locations. Each will link to inventory page."""

    model = Location
    template_name = 'location/list_location.html'

    def get_queryset(self):
        return super(ListLocationView, self).get_queryset()
        # return qs.filter(start_time__gt=timezone.now()).order_by('start_time')


class UpdateLocationView(UpdateView):
    """View for updating a location."""

    model = Location
    form_class = CreateLocationForm
    template_name = 'location/update_location.html'

    def get_success_url(self):
        messages.success(self.request, 'Location updated successfully.')
        return reverse('location:list_locations')


class DeleteLocationView(DeleteView):
    """Delete View for a location."""

    model = Location
    template_name = 'location/delete_location.html'

    def get_success_url(self):
        messages.success(self.request, 'Location removed successfully.')
        return reverse('location:list_locations')
