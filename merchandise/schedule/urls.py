from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^user_landing/', views.UsersLandingView.as_view(), name='user_landing'),
    url(r'^create_schedule/', views.CreateScheduleView.as_view(), name='create_schedule'),
    url(r'^list_schedules/', views.ListScheduleView.as_view(), name='list_schedules'),
    url(r'^update_schedule/(?P<pk>\d+)/', views.UpdateScheduleView.as_view(), name='update_schedule'),
    url(r'^delete_schedule/(?P<pk>\d+)/', views.DeleteScheduleView.as_view(), name='delete_schedule'),
]