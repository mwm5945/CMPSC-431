from django.contrib import messages

from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from .models import Shift
from .forms import CreateScheduleForm


class CreateScheduleView(CreateView):
    """Create View for adding a schedule."""

    model = Shift
    form_class = CreateScheduleForm
    template_name = 'schedule/create_schedule.html'
    success_url = reverse_lazy('users:list_schedules')

    params = {
        'page_header': "Add a Schedule"
    }

    def get_context_data(self, **kwargs):
        """Returns context for the."""
        context = super(CreateScheduleView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class ListScheduleView(ListView):
    """View for showing all schedules."""

    model = Shift
    template_name = 'schedule/list_schedule.html'

    params = {
        'page_header': "User Schedules"
    }

    def get_context_data(self, **kwargs):
        """Returns context for the."""
        context = super(ListScheduleView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context


class UpdateScheduleView(UpdateView):
    """View for updating a schedule."""

    model = Shift
    form_class = CreateScheduleForm
    template_name = 'schedule/update_schedule.html'

    params = {
        'page_header': "Update a Schedule"
    }

    def get_success_url(self):
        messages.success(self.request, 'Schedule updated successfully.')
        return reverse('users:list_schedules')


    def get_context_data(self, **kwargs):
        """Returns context for the."""
        context = super(UpdateScheduleView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context

class DeleteScheduleView(DeleteView):
    """Delete View for a schedule."""

    model = Shift
    template_name = 'schedule/confirm_delete_schedule.html'

    params = {
        'page_header': "Delete a Schedule"
    }

    def get_success_url(self):
        messages.success(self.request, 'Schedule removed successfully.')
        return reverse('users:list_schedules')

    def get_context_data(self, **kwargs):
        """Returns context for the."""
        context = super(DeleteScheduleView, self).get_context_data(**kwargs)
        context.update(self.params)
        return context
