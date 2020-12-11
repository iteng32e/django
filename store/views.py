from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from . import models, forms


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


def shopping_form_view(request):
    form = forms.ShopForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            shop = form.save(commit=False)
            shop.amount = form.cleaned_data.get('amount')
            shop.number = form.cleaned_data.get('number')
            shop.method = form.cleaned_data.get('method')
            shop.save()
            return redirect(reverse('store:product_list_url'))
    else:
        form = forms.ShopForm()
        return render(request, 'store/shop/shop.html', {'form': form})
