from django.db import models



class Sale(Model):
    """Individual item sale."""

    # id inluded
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey('Item')
    transaction = models.ForeignKey('Transaction')


class Transaction(Model):
    """Complete transaction for a customer."""

    TRANSACTION_STATUS = models.(
        ('Paid', 'Paid'),
        ('Returned', 'Returned')
    )

    TRANSACTION_TYPE = models.(
        ('Online', 'Online'),
        ('In Store', 'In Store'),
        ('Other', 'Other')
    )

    # id included
    status = models.CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_STATUS)
    transaction_type = models.CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_TYPE)
    date_time = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey('Customer')
    completed_by = models.ForeignKey('ThinkUser')