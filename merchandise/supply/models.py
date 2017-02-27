from django.db import models


class Order(models.Model):
    """Merchandise order to restock inventory."""

    ORDER_STATUS = (
        ('Ordered', 'Ordered'),
        ('In Transit', 'In Transit'),
        ('Arrived', 'Arrived'),
        ('Moved to Storage', 'Moved to Storage')
    )

    status = models.CharField(max_length=10, choices=ORDER_STATUS)
    date = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL)
    processed_by = models.ForeignKey('ThinkUser', on_delete=models.SET_NULL)
