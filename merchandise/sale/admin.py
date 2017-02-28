from django.contrib import admin
from sale.models import Sale, Transaction


class SaleAdmin(admin.ModelAdmin):
    """Admin for Sale model."""

    list_display = ['id', 'price', 'status', 'item', 'transaction', 'inventory_transaction']


class TransactionAdmin(admin.ModelAdmin):
    """Admin for Transaction model."""

    list_display = ['id', 'transaction_type', 'timestamp', 'customer', 'completed_by']


admin.site.register(Sale, SaleAdmin)
admin.site.register(Transaction, TransactionAdmin)