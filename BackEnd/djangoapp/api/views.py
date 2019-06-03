from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import HttpResponse
import json
import ast
from datetime import datetime
from .models import Tanks_Overall_Status, Tank, Quality_Avg
from .models import Naphtha_Plan_All_Months, Naphtha_Plan_Single_Month, Quality_Real
# new line


#Quality_Avg
#have to define



#@csrf_exempt
#def createlogin(request):
#   print("in updateLogin")
 #  login_data = JSONParser().parse(request)
  # print(login_data)
   #login_serializer = LoginSerializer(data=login_data)
   
   #if login_serializer.is_valid():
   #   login_serializer.save() # data base saved
    #  return JsonResponse(login_serializer.data, status=status.HTTP_201_CREATED) 
  # return JsonResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def getSuctionBlending(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')

      parent_obj = list(parent_obj.values())
      

      return JsonResponse(parent_obj[0], safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getReceivingNaphtha(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]

      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj)
      recevingtanks = []
      for i in range(0,len(tank)):
            if tank[i].Receiving_Naphtha == True:
                  recevingtanks.append(tank[i].Tank_No)

      #recevingtanks = list(recevingtanks.values())

      return JsonResponse(recevingtanks, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getAllTanks(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]

      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj)
      tanklevels = []
      for i in range(0,len(tank)):
            tanklevels.append(tank[i].Level)

      return JsonResponse(tanklevels, safe = False, status=status.HTTP_201_CREATED)


@csrf_exempt
def getQualityAvg(request, tankno):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = tankno).get()
      quality_avg = Quality_Avg.objects.filter(tank = tank)

      quality_avg = list(quality_avg.values())
      
      print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(quality_avg[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getQualityReal(request, tankno):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = tankno).get()
      quality_real = Quality_Real.objects.filter(tank = tank)

      quality_real = list(quality_real.values())
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(quality_real[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getClickedTank(request, tankno):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = tankno)

      tank = list(tank.values())
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(tank[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getComingMonthPlan(request):
      
      parent_obj = Naphtha_Plan_All_Months.objects.all().order_by('-id')[0]
      
      monthplan = Naphtha_Plan_Single_Month.objects.filter(naphtha_Plan_All_Months = parent_obj)

      monthplan = list(monthplan.values())
      
      print ("*****************" + str(monthplan) + "******************")

      return JsonResponse(monthplan , safe = False, status=status.HTTP_201_CREATED)


@csrf_exempt
def getAnyMonthPlan(request, fromdate, todate):

      parent_obj = Naphtha_Plan_All_Months.objects.all().order_by('-id')[0]
      
      monthplan = Naphtha_Plan_Single_Month.objects.filter(naphtha_Plan_All_Months = parent_obj)

      monthplan = list(monthplan.values())

      fromdate = datetime.strptime(fromdate, "%Y-%m-%d")
      todate = datetime.strptime(todate, "%Y-%m-%d")

      frommonth = fromdate.month
      fromyear = fromdate.year
      tomonth = todate.month
      toyear = todate.year
      
      array = Naphtha_Plan_All_Months.objects.all()

      plan = []

      for i in range(0,len(array)):
            M = datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").month
            Y = datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").year
            if M >= frommonth and Y >= fromyear and M <= tomonth and Y <= toyear:
                  arraymonth = Naphtha_Plan_Single_Month.objects.filter(naphtha_Plan_All_Months = array[i])
                 # for k in range(0,len(arraymonth)):
                  plan.append(list(arraymonth.values()))
                  
      
      return JsonResponse(plan, safe = False, status=status.HTTP_201_CREATED)           