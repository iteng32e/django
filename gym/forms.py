from django import forms
from club import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ('name', 'text',)
