from django.conf.urls import url
from item import views

app_name = 'item'
urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$', 
        views.ItemDetailsDetailView.as_view(), 
        name='item_details_detail'),
    url(r'^$',
        views.ItemDetailsListView.as_view(),
        name='item_details_list'),
]