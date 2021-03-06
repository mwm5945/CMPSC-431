from django.db import models
from django.contrib.auth.models import AbstractUser

from sale.models import Transaction


class Address(models.Model):
    """Address."""

    line_one = models.CharField(max_length=255)
    line_two = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.SmallIntegerField()

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        if self.line_two:
            return "{0} {1}, {2}, {3} {4}".format(self.line_one, self.line_two, self.city, self.state, self.zip)
        else:
            return "{0}, {1}, {2} {3}".format(self.line_one, self.city, self.state, self.zip)



class Customer(models.Model):
    """Merchandise customers."""

    email = models.EmailField()
    address = models.ForeignKey('directory.Address', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.email

    @property
    def sale_total(self):
        total = 0

        for trans in self.transaction_set.all():
            total += trans.total
        
        return total


class Supplier(models.Model):
    """Merchandise supplier."""

    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    address = models.ForeignKey('directory.Address', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


class MerchandiseUser(AbstractUser):
    """Merchandise user."""
    
    class Meta:
        verbose_name = 'Merchandise User'
        verbose_name_plural = 'Merchandise Users'

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name