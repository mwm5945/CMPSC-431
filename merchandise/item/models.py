from django.db import models



class Item(Model):
    """Merchandise inventory."""

    MERCH_INVENTORY_SIZES = models.(
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    )

    sku = models.SmallIntegerField(null=False, blank=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(required=)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=11, null=True, blank=True, choices=MERCH_INVENTORY_SIZES)
    category = models.ForeignKey('ItemCategory', on_delete=SET_NULL)


class ItemCategory(Model):
    """Item category."""

    # id included
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('ItemCategory', on_delete=CASCADE)
