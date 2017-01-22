from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SupplyLogisticsView.as_view(), name='supply_logistics'),
    url(r'^merch-inventory-home/$', views.MerchInventoryLandingView.as_view(), name='merch-inventory-home'),
    url(r'^merch-inventory-add/$', views.MerchInventoryAddItemView.as_view(), name='merch-inventory-add'),
    url(r'^merch-inventory-remove/(?P<pk>\d+)/$', views.MerchInventoryDeleteItemView.as_view(),
        name='merch-inventory-remove'),
    url(r'^merch-inventory-update/(?P<pk>\d+)/$', views.MerchInventoryItemUpdateView.as_view(),
        name='merch-inventory-update'),
    url(r'^merch-inventory-item-detail/(?P<pk>\d+)/$', views.MerchInventoryItemDetailView.as_view(),
        name='merch-inventory-item-detail'),
]
