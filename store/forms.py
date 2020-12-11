from django import forms
from . import models


class ShopForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = ('amount', 'number', 'method',)
