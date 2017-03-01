from django.db import models


class Item(models.Model):
    """Merchandise inventory."""

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XL = 'XL'
    XXL = '2X'
    XXXL = '3X'
    XXXXL = '4X'
    YOUTH_SMALL = 'YS'
    YOUTH_MEDIUM = 'YM'
    YOUTH_LARGE = 'YL'

    SIZE_CHOICES = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XL, 'XL'),
        (XXL, 'XXL'),
        (XXXL, 'XXXL'),
        (XXXXL, 'XXXXL'),
        (YOUTH_SMALL, 'Youth Small'),
        (YOUTH_MEDIUM, 'Youth Medium'),
        (YOUTH_LARGE, 'Youth Large')
    )

    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    sku = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)
    size = models.CharField(max_length=2, null=True, blank=True, choices=SIZE_CHOICES)
    category = models.ForeignKey('item.ItemCategory', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class ItemCategory(models.Model):
    """Item category."""

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('item.ItemCategory', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'
