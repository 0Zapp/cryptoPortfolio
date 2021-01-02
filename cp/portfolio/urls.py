from django.urls import path, re_path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('currencies/', views.currencies, name='currencies'),
    path('currencies/<int:id>/', views.currency, name='currency'),
    path('currency/edit/<int:id>/', views.edit, name='edit'),
    path('currency/new/', views.new, name='new'),
    path('transaction/<int:id>/', views.transaction, name= 'transaction')
]
