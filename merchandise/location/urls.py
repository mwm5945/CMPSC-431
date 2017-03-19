from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create_location/', views.CreateLocationView.as_view(), name='create_location'),
    url(r'^list_locations/', views.ListLocationView.as_view(), name='list_locations'),
    url(r'^update_location/(?P<pk>\d+)/', views.UpdateLocationView.as_view(), name='update_location'),
    url(r'^delete_location/(?P<pk>\d+)/', views.DeleteLocationView.as_view(), name='delete_location'),
]

