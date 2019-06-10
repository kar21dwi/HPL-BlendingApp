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
   path('runninginput/', views.getRunningInput),
   path('profitmaxinput/', views.getProfitMaxInput),
   path('bestfitinput/', views.getBestFitInput),
   path('nexthourinput/', views.getNextHourInput),
   path('niractual/', views.getNirActual),
   path('nirmodel/', views.getNirModel),
   path('userdefinedinputs/', views.postUserDefinedInputs),
   path('userdefinedoutput/', views.getUserDefinedOutput),
   path('runningoutput/', views.getRunningOutput),
   path('profitmaxoutput/', views.getProfiitMaxOutput),
   path('bestfitoutput/', views.getBestFitOutput),
   path('nexthouroutput/', views.getNextHourOutput),
   path('nexthourselectionupdate/<selection>/', views.updateNextHourSelection),
   path('comingmonthplan/', views.getComingMonthPlan),
   path('anymonthplan/<fromdate>/<todate>/', views.getAnyMonthPlan),
   path('thismonthdetail/', views.getThisMonthDetail),
   path('anymonthdetail/<fromdate>/<todate>/', views.getAnyMonthDetail),
   path('monthplan/', views.postNaphthaMonthPlan),
   path('newnaphtha/', views.PostNewNaphthaDetails),
   path('receivednaphtha/', views.GetReceivedNaphtha),
   path('transfernaphthaquantity/', views.transferNaphthaQuantity),
   path('inputoutput/<fromdate>/<todate>/', views.getInputOutput),
   path('qualityquantity/<fromdate>/<todate>/', views.getQualityQuantity),

   # path('login/', views.createlogin)


]