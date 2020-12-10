from django.shortcuts import render
from django.views import generic

from . import models


class ProductLisView(generic.ListView):
    model = models.Product
    template_name = 'store/product/product_list.html'


def product_detail_def(request, id):
    model = models.Product.objects.filter(pk=id)
    context = {'object_list': model}
    return render(request, 'store/product/product_detail.html', context)


class PaymentListView(generic.ListView):
    model = models.Payment
    template_name = 'store/payment/payment_list.html'


def payment_detail_def(request, id):
    model = models.Payment.objects.filter(pk=id)
    context = {'object_list': model}
    return render(request, 'store/payment/payment_detail.html', context)
