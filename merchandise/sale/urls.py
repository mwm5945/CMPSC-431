from django.conf.urls import url
from sale import views

app_name = 'sale'
urlpatterns = [
    url(r'^transaction/receipt/(?P<pk>[-\w]+)/$', 
        views.TransactionReceiptDetailView.as_view(), 
        name='transaction_receipt_detail'),
    url(r'^transaction/(?P<pk>[-\w]+)/$', 
        views.TransactionDetailView.as_view(), 
        name='transaction_detail'),
    url(r'^return/(?P<pk>[-\w]+)/$', 
        views.SaleReturnView.as_view(), 
        name='sale_return'),
    url(r'^cart/$',
        views.CartView.as_view(),
        name='cart'),
    url(r'^clear/$',
        views.clear_cart,
        name='sale_clear'),
    url(r'^complete/$',
        views.TransactionCreateView.as_view(),
        name='transaction_create'),
    url(r'^(?P<pk>[-\w]+)/$', 
        views.SaleDetailView.as_view(), 
        name='sale_detail'),
    url(r'^$',
        views.TransactionListView.as_view(),
        name='sale_list'),
]