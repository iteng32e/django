from django.db import models
from django.db.models.functions import Lower

from club.models import Member


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=7, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    sold_number = models.IntegerField(default=0, null=True, blank=True)
    img_url = models.TextField(max_length=300, null=True, blank=True)
    """ موجود یا عدم موجودیت کالا """
    STATUS = (
        ('EXIST', 'Exist'),
        ('NOT_EXIST', 'Not_Exist'),
    )
    status = models.CharField(default='EXIST', max_length=9, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    METHOD = (
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
    )
    method = models.CharField(choices=METHOD, default='ONLINE', max_length=7, null=True, blank=True)
    STATUS = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
    status = models.CharField(choices=STATUS, default='ACTIVE', max_length=8, null=True, blank=True)
    description = models.TextField(help_text="Reason of Activate or Inactivate of method", null=True, blank=True)

    def __str__(self):
        str1 = self.method + ", "
        str2 = self.status
        str3 = str1 + str2
        return str3


class Payment(models.Model):
    payer = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.CharField(max_length=8, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    number = models.PositiveIntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        str1 = self.payer.first_name + " ,"
        str2 = self.product.name
        str3 = str1 + str2
        return str3

    def get_ordering(self, request):
        return [Lower('payer.first_name')]

