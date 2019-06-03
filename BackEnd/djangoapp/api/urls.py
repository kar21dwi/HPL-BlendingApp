from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers
from djangoapp.api import views
from django.urls import reverse



urlpatterns = [

   path('suctionblending/', views.getSuctionBlending),
   path('qualityavg/<tankno>/', views.getQualityAvg), 
   path('comingmonthplan/', views.getComingMonthPlan),
   path('anymonthplan/<fromdate>/<todate>/', views.getAnyMonthPlan),

   # path('login/', views.createlogin)


]