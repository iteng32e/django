from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass



