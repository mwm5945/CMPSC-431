from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Inventory(models.Model):
    """Inventory of a certain item."""

    quantity = models.IntegerField(default=0)
    item = models.ForeignKey('item.Item', on_delete=models.CASCADE)
    location = models.ForeignKey('location.Location', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
        unique_together = ('item', 'location')

    def __str__(self):
        return self.item.name + " " +  self.item.get()
        

class InventoryTransaction(models.Model):
    """Change in inventory."""

    inventory = models.ForeignKey('inventory.Inventory', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Inventory Transaction'
        verbose_name_plural = 'Inventory Transactions'

    @staticmethod
    def add_to_inventory(item, location, quantity, user=None):
        """Adds the specified quantity to inventory at the given location."""

        try:
            inventory = Inventory.objects.get(item=item, location=location)
            inventory.quantity += quantity
            inventory.save()
        except ObjectDoesNotExist:
            inventory = Inventory.objects.create(item=item, location=location, quantity=quantity)

        transaction = InventoryTransaction.objects.create(inventory=inventory, quantity=quantity, user=user)

        return transaction
    
    @staticmethod
    def remove_from_inventory(item, location, quantity, user=None):
        """Removes the specified quantity from inventory at the given location."""

        quantity = -quantity

        return InventoryTransaction.add_to_inventory(item=item, location=location, quantity=quantity, user=user)

    @staticmethod
    def move_inventory(item, from_location, to_location, quantity, user=None):
        """Moves the number of items in inventory from one location to another."""

        remove_from = InventoryTransaction.remove_from_inventory(
                        item=item, location=from_location, quantity=quantity, user=user)
        
        add_to = InventoryTransaction.add_to_inventory(
                    item=item, location=to_location, quantity=quantity, user=user)

        remove_from.pair_transaction = add_to
        add_to.pair_transaction = remove_from
        
        return (remove_from, add_to)
