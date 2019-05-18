from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers
from djangoapp.api import views



urlpatterns = [

    path('tanks/', views.getTanks),
    path('login/', views.createlogin)


]