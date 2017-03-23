from django.conf.urls import url
from supply import views

app_name = 'order'
urlpatterns = [
    url(r'^(?P<pk>[-\w]+)/$',
        views.OrderDetailView.as_view(),
        name='order_detail'),
    url(r'^$',
        views.OrderListView.as_view(),
        name='order_list'),
]