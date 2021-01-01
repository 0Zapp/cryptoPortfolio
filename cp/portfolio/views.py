from django.shortcuts import render
from django.http import HttpResponse


def index(request):
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


def hello(requset):
    return render(requset, 'hello.html')
