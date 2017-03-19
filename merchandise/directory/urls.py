from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^supplier/$', views.SupplierListView.as_view(), name='supplier'),
    url(r'^supplier/submission$', views.SupplierSubmissionView.as_view(), name='supplier-submission'),
    url(r'^supplier/detail/$', views.SupplierDetailView.as_view(), name='supplier-detail'),
    url(r'^supplier/update/$', views.SupplierUpdateView.as_view(), name='supplier-update')
]
