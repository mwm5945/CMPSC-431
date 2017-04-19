from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/', views.LocationCreateView.as_view(), name='location_create'),
    url(r'^update/(?P<pk>\d+)/', views.LocationUpdateView.as_view(), name='location_update'),
    url(r'^(?P<pk>\d+)/', views.LocationDetailView.as_view(), name='location_detail'),
    url(r'^$', views.LocationListView.as_view(), name='locations'),
]

