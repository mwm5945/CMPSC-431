from django.conf.urls import url
from django.urls import reverse
from inventory import views

app_name = 'inventory'
urlpatterns = [
    url(r'^create/$',
        views.CreateInventory.as_view(),
        name='inventory_create'),
    url(r'^list/$',
        views.ListInventory.as_view(),
        name='inventory_list'),
    url(r'^update/(?P<pk>[-\w]+)/$',
        views.UpdateInventory.as_view(),
        name='inventory_update'),
    url(r'^move/$',
        views.CreateInventoryTransaction.as_view(),
        name='move'),
    url(r'list_moves/$',
        views.ListInventoryTransactions.as_view(),
        name='list_moves'),
    # url(r'^(?P<pk>[-\w]+)/add_size/$',
    #     views.ItemCreateView.as_view(),
    #     name='item_create'),
    # url(r'^$',
    #     views.ItemDetailsView.as_view(),
    #     name='item_details'),
]