from django.db import models

from inventory.models import InventoryTransaction


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

    @staticmethod
    def new_sale(item, price, transaction, location, status=PAID):
        inventory_transaction = InventoryTransaction.remove_from_inventory(
            item=item,
            location=location,
            quantity=1,
            user=transaction.completed_by
        )

        sale = Sale.objects.create(
            price=price,
            status=status,
            item=item,
            transaction=transaction,
            inventory_transaction=inventory_transaction
        )

        return sale
    
    def return_sale(self, location, user):
        if self.status is not Sale.RETURNED:
            inventory_transaction = InventoryTransaction.add_to_inventory(
                item=self.item,
                location=location,
                quantity=1,
                user=user
            )
            self.inventory_transaction = inventory_transaction
            self.status = Sale.RETURNED
            self.save()

        return self
        

class Transaction(models.Model):
    """Complete transaction for a customer."""

    ONLINE = 'O'
    STORE = 'S'
    OTHER = 'X'

    TRANSACTION_TYPE_CHOICES = (
        (STORE, 'In Store'),
        (ONLINE, 'Online'),
        (OTHER, 'Other')
    )

    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('directory.Customer', null=True, blank=True, on_delete=models.SET_NULL)
    completed_by = models.ForeignKey('directory.MerchandiseUser', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    @staticmethod
    def new_transaction(items, transaction_type, customer, user, location):
        """Creates a new transaction."""

        transaction = Transaction.objects.create(
            transaction_type=transaction_type, 
            customer=customer, 
            completed_by=user
        )

        for item in items:
            Sale.new_sale(
                item=item,
                price=item.price,
                transaction=transaction,
                location=location
            )
        
        return transaction
    
    @property
    def total(self):
        total = 0

        for sale in self.sale_set.all():
            total += sale.price
        
        return total
