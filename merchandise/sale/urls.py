from django.conf.urls import url
from sale import views

app_name = 'sale'
urlpatterns = [
    url(r'^clear/$',
        views.clear_cart,
        name='sale_clear'),
    url(r'^$',
        views.SaleView.as_view(),
        name='sale'),
]