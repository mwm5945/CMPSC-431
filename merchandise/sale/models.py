from django.db import models


class Sale(models.Model):
    """Individual item sale."""

    PAID = 'P'
    RETURNED = 'R'

    STATUS_CHOICES = (
        (PAID, 'Paid'),
        (RETURNED, 'Returned')
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    item = models.ForeignKey('item.Item', null=True, blank=True, on_delete=models.SET_NULL)
    transaction = models.ForeignKey('sale.Transaction', on_delete=models.CASCADE)
    inventory_transaction = models.ForeignKey('inventory.InventoryTransaction', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'


class Transaction(models.Model):
    """Complete transaction for a customer."""

    ONLINE = 'O'
    STORE = 'S'
    OTHER = 'X'

    TRANSACTION_TYPE_CHOICES = (
        (ONLINE, 'Online'),
        (STORE, 'In Store'),
        (OTHER, 'Other')
    )

    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('directory.Customer', null=True, blank=True, on_delete=models.SET_NULL)
    completed_by = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'