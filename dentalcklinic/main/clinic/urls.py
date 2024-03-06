from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('price', views.price),
    path('contacts', views.contacts),
]
