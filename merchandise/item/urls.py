from django.conf.urls import url
from django.urls import reverse
from item import views

app_name = 'item'
urlpatterns = [
    url(r'^create/$', 
        views.ItemDetailsCreateView.as_view(), 
        name='item_details_create'),
    url(r'^update/(?P<pk>[-\w]+)/$', 
        views.ItemDetailsUpdateView.as_view(), 
        name='item_details_update'),
    url(r'^(?P<pk>[-\w]+)/$', 
        views.ItemDetailsDetailView.as_view(), 
        name='item_details_detail'),
    url(r'^(?P<pk>[-\w]+)/add_size/$', 
        views.ItemCreateView.as_view(), 
        name='item_create'),
    url(r'^$',
        views.ItemDetailsListView.as_view(),
        name='item_details_list'),
]