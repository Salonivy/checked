from django.contrib import admin
from django.urls import path,include
from myapp2 import views

urlpatterns = [
    path('show',views.index, name='index')
]
