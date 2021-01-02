from django.forms import ModelForm, Form
import django.forms as f
from .models import Currency


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = ['name', 'description']

