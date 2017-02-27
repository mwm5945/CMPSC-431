from django.db.models import Model



MERCH_INVENTORY_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large')
)


class Item(Model):
    """Merchandise inventory."""

    sku = SmallIntegerField(null=False, blank=False)
    name = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    is_active = BooleanField(required=)
    description = TextField(blank=True, null=True)
    size = CharField(max_length=11, null=True, blank=True, choices=MERCH_INVENTORY_SIZES)
    category = ForeignKey('ItemCategory', on_delete=SET_NULL)


class ItemCategory(Model):
    """Item category."""

    # id included
    name = CharField(max_length=255)
    parent_category = ForeignKey('ItemCategory', on_delete=CASCADE)
