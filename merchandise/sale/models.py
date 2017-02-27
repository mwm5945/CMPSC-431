from django.db.models import Model

TRANSACTION_STATUS = (
    ('Paid', 'Paid'),
    ('Returned', 'Returned')

)

TRANSACTION_TYPE = (
    ('Online', 'Online'),
    ('In Store', 'In Store'),
    ('Other', 'Other')
)


class Sale(Model):
    """Individual item sale."""

    # id inluded
    price = DecimalField(max_digits=10, decimal_places=2)
    item = ForeignKey('Item')
    transaction = ForeignKey('Transaction')


class Transaction(Model):
    """Complete transaction for a customer."""

    # id included
    status = CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_STATUS)
    transaction_type = CharField(max_length=10, null=False, blank=False, choices=TRANSACTION_TYPE)
    date_time = DateTimeField(auto_now=True)
    customer = ForeignKey('Customer')
    completed_by = ForeignKey('ThinkUser')