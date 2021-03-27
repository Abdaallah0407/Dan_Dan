
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url('basket_adding/', views.basket_adding, name='basket_adding'),

]
