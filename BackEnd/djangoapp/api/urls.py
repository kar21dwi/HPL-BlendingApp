from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers
from djangoapp.api import views
from django.urls import reverse



urlpatterns = [

   path('suctionblending/', views.getSuctionBlending),
   path('receivingnaphtha/', views.getReceivingNaphtha),
   path('alltanks/', views.getAllTanks),
   path('qualityavg/<tankno>/', views.getQualityAvg), 
   path('qualityreal/<tankno>/', views.getQualityReal),
   path('clickedtank/<tankno>/', views.getClickedTank),
   path('comingmonthplan/', views.getComingMonthPlan),
   path('anymonthplan/<fromdate>/<todate>/', views.getAnyMonthPlan),

   # path('login/', views.createlogin)


]