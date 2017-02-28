from django.db import models


class Inventory(models.Model):
    """Inventory of a certain item."""

    quantity = models.IntegerField(default=0)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'


class InventoryTransaction(models.Model):
    """Change in inventory."""

    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Inventory Transaction'
        verbose_name_plural = 'Inventory Transactions'
