from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='poruke_index'),
    path('int/broj-<int:broj>/', views.broj, name='poruke_broj'),
    path('string/<str:rec>/', views.rec, name='poruke_rec'),
    re_path(r'^regex/(?:godina-(?P<godina>[0-9]{4}))/(?:mesec-(?P<mesec>[0-9]{2}))/$', views.regex, name='poruke_regex'),
    path('parametri/', views.parametri, name='poruke_parametri'),
    path('hello/', views.hello, name='poruke_hello')
]
