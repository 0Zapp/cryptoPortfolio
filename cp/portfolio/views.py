from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Currency
from .forms import CurrencyForm
from .forms import TransactionForm
from .models import Transaction
from json import dumps

def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Crypto Portfolio'})
    else:
        return redirect('portfolio:currencies')


@login_required
def currencies(req):
    tmp = Currency.objects.all()
    collection = [['Currency', 'Number of Transactions']]

    for i in range(len(tmp)):
        collection.append([tmp[i].name,len(tmp[i].transaction_set.all())])
    
    collection = dumps(collection)
    return render(req, 'currencies.html', {'currencies': tmp, 'pie':collection})


@login_required
def currency(req, id):
    tmp = get_object_or_404(Currency, id=id)
    transactions = tmp.transaction_set.all()
    collection = []
    for i in range(len(transactions)):
        collection.append([i+1,transactions[i].amount])
    collection = dumps(collection)
    return render(req, 'currency.html', {'currency': tmp, 'page_title': tmp.name, 'transactions': transactions, 'chart':collection})


@permission_required('portfolio.change_currency')
def edit(req, id):
    if req.method == 'POST':
        form = CurrencyForm(req.POST)

        if form.is_valid():
            a = Currency.objects.get(id=id)
            a.name = form.cleaned_data['name']
            a.description = form.cleaned_data['description']
            a.save()
            return redirect('portfolio:currencies')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Currency.objects.get(id=id)
        form = CurrencyForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('portfolio.add_currency')
def new(req):
    if req.method == 'POST':
        form = CurrencyForm(req.POST)

        if form.is_valid():
            a = Currency(name=form.cleaned_data['name'], description=form.cleaned_data['description'])
            a.save()
            return redirect('portfolio:currencies')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = CurrencyForm()
        return render(req, 'new.html', {'form': form})

@permission_required('portfolio.add_transaction')
def transaction(req, id):
    tmp = get_object_or_404(Currency, id=id)
    if req.method == 'POST':
        form = TransactionForm(req.POST)

        if form.is_valid():
            a = Transaction(adressFrom=form.cleaned_data['adressFrom'], amount=form.cleaned_data['amount'], adressTo=form.cleaned_data['adressTo'], currency=Currency.objects.get(id=id))
            a.save()
            return redirect('portfolio:currencies')
        else:
            return render(req, 'newTransaction.html', {'currency': tmp,'form': form})
    else:
        form = TransactionForm()
        return render(req, 'newTransaction.html', {'currency': tmp,'form': form})