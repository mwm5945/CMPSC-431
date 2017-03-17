from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView

from .models import Shift
from .forms import CreateScheduleForm

class UsersLandingView(TemplateView):
    """Landing Page for users."""

    template_name = 'schedule/users_landing.html'


class CreateScheduleView(CreateView):
    """Create View for adding a schedule."""

    model = Shift
    form_class = CreateScheduleForm
    template_name = 'schedule/create_schedule.html'
    success_url = reverse_lazy('users:list_schedules')


class ListScheduleView(ListView):
    """View for showing all schedules."""

    model = Shift
    template_name = 'schedule/list_schedule.html'

    def get_queryset(self):
        qs = super(ListScheduleView, self).get_queryset()
        return qs.filter(start_time__gt=timezone.now()).order_by('start_time')


class UpdateScheduleView(UpdateView):
    """View for updating a schedule."""

    model = Shift
    form_class = CreateScheduleForm
    template_name = 'schedule/update_schedule.html'

    def get_success_url(self):
        messages.success(self.request, 'Schedule updated successfully.')
        return reverse('users:list_schedules')

class DeleteScheduleView(DeleteView):
    """Delete View for a schedule."""

    model = Shift
    template_name = 'schedule/confirm_delete_schedule.html'

    def get_success_url(self):
        messages.success(self.request, 'Schedule removed successfully.')
        return reverse('users:list_schedules')