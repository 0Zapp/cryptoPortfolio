from django.forms import ModelForm, Form
import django.forms as f
from .models import Currency
from .models import Transaction


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = ['name', 'description']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['adressFrom', 'amount','adressTo']

