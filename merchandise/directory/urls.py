from django.conf.urls import url
from directory import views


urlpatterns = [
    url(r'^customer/update/(?P<pk>\d+)$', 
        views.CustomerUpdateView.as_view(), 
        name='customer_update'),
    url(r'^customer/(?P<pk>\d+)$', 
        views.CustomerDetailView.as_view(), 
        name='customer_detail'),
    url(r'^customer/', 
        views.CustomerListView.as_view(), 
        name='customer_list'),
]
