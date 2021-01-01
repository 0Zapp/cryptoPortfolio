from django.contrib import admin
from .models import Currency, Transaction

admin.site.register(Currency)
admin.site.register(Transaction)