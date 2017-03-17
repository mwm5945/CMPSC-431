from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user_landing/', views.UsersLandingView.as_view(), name='user_landing'),
    url(r'^create_schedule/', views.CreateScheduleView.as_view(), name='create_schedule'),
]