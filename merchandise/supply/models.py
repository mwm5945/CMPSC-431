from django.db import models


class Order(models.Model):
    """Merchandise order to restock inventory."""

    ORDERED = 'O'
    IN_TRANSIT = 'I'
    ARRIVED = 'A'
    STORAGE = 'S'

    ORDER_STATUS = (
        (ORDERED, 'Ordered'),
        (IN_TRANSIT, 'In Transit'),
        (ARRIVED, 'Arrived'),
        (STORAGE, 'Moved to Storage')
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDERED)
    supplier = models.ForeignKey('directory.Supplier', null=True, blank=True, on_delete=models.SET_NULL)
    timestamp = models.DateTimeField(auto_now_add=True)
    entered_by = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL, related_name='order_entered_by')
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL, related_name='order_last_updated_by')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
