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
from .models import Tanks_Overall_Status, Tank, Quality_Avg
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
def getQualityAvg(request, tankno):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = tankno).get()
      quality_avg = Quality_Avg.objects.filter(tank = tank)

      quality_avg = list(quality_avg.values())
      
      print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(quality_avg , safe = False, status=status.HTTP_201_CREATED)