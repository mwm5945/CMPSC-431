from django.db import models


class ItemDetails(models.Model):
    """Merchandise item details."""

    name = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    category = models.ForeignKey('item.ItemCategory', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Item Details'
        verbose_name_plural = 'Item Details'
    
    def __str__(self):
        return self.name
    
    @property
    def sizes(self):
        return self.item_set


class Item(models.Model):
    """Merchandise item."""

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

    sku = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=2, null=True, blank=True, choices=SIZE_CHOICES)
    details = models.ForeignKey('item.ItemDetails', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return "{0} - {1}".format(self.name, self.get_size_display())

    @property
    def name(self):
        return self.details.name
    
    @property
    def description(self):
        return self.details.description

    @property
    def category(self):
        return self.details.category

    @property
    def is_active(self):
        return self.details.is_active


class ItemCategory(models.Model):
    """Item category."""

    name = models.CharField(max_length=255)
    parent = models.ForeignKey('item.ItemCategory', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'

    def __str__(self):
        return self.name
