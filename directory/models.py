from django.db.models import Model


class Address(Model):
    """Address."""

    line_one = CharField(max_length=255)
    line_two = CharField(max_lenght=255)
    city = CharField(max_length=255)
    state = CharField(max_length=2)
    zip = SmallIntegerField()


class Customer(Model):
    """Merchandise customers."""

    # id included
    email = EmailField()
    address = ForeignKey('Address', null=True, blank=True)


class Supplier(Model):
    """Merchandise supplier."""

    phone = CharField(max_length=10)
    name = CharField(max_length=255)
    address = ForeignKey('Address')


class User(Model):
    """Merchandise user."""

    name = CharField(max_length=255)
    username = CharField(max_length=255)
    password = CharField(max_lenght=255)
    email = EmailField()