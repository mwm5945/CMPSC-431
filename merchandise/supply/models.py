from django.db.models import Model


ORDER_STATUS = (
    ('Ordered', 'Ordered'),
    ('In Transit', 'In Transit'),
    ('Arrived', 'Arrived'),
    ('Moved to Storage', 'Moved to Storage')
)


class Order(Model):
    """Merchandise order to restock inventory."""

    status = CharField(max_length=10, choices=ORDER_STATUS)
    date = DateTimeField(auto_now=True)
    supplier = ForeignKey('Supplier', on_delete=SET_NULL)
    processed_by = ForeignKey('ThinkUser', on_delete=SET_NULL)
