from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Currency
from .forms import CurrencyForm


def hello(request):
    return HttpResponse('Hello Django')


def broj(request, broj):
    return HttpResponse('Uneli ste borj: ' + str(broj))


def rec(request, rec):
    return HttpResponse('Uneli ste rec: ' + rec)


def tekst(request, tekst):
    return HttpResponse('Uneli ste: ' + tekst)


def regex(request, godina, mesec):
    return HttpResponse('Uneli ste godinu: ' + str(godina) + ' i mesec: ' + str(mesec))


def parametri(request):
    return HttpResponse('Uneti parametri su: ' + str([str(k) + ': ' + str(v) for k, v in request.GET.items()]))


def helloPage(requset):
    return render(requset, 'hello.html')

def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Vezbe 13'})
    else:
        return redirect('portfolio:currencies')


@login_required
def currencies(req):
    tmp = Currency.objects.all()
    return render(req, 'currencies.html', {'currencies': tmp})


@login_required
def currency(req, id):
    tmp = get_object_or_404(Currency, id=id)
    return render(req, 'currency.html', {'currency': tmp, 'page_title': tmp.title})


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