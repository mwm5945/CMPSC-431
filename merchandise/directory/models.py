from django.db import models


class Address(Model):
    """Address."""

    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_lenght=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.SmallIntegerField()


class Customer(Model):
    """Merchandise customers."""

    # id included
    email = models.EmailField()
    address = models.ForeignKey('Address', null=True, blank=True)


class Supplier(Model):
    """Merchandise supplier."""

    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    address = models.ForeignKey('Address')


class User(Model):
    """Merchandise user."""

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_lenght=255)
    email = models.EmailField()