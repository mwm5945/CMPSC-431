from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView

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
    success_url = reverse_lazy('users:user_landing')



class ReadScheduleView(ListView):
    """View for showign all schedules."""

    model = Shift