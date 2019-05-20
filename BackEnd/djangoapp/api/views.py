from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TankSerializer, LoginSerializer
from .models import Tank
from rest_framework.response import Response
from rest_framework.request import Request
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.http import HttpResponse
from .models import Tank
from .models import Login
# new line

@csrf_exempt
def getTanks(request):
   #tanks = Tank.objects.all()
   #print(tanks[0].Avg_Quality)
   print("inside getTanks")
   tanks = list(Tank.objects.values())
   print(tanks)
   return JsonResponse(tanks, safe=False)
   
   #if tank_serializer.is_valid():
   #   tank_serializer.save() # data base saved
    # return JsonResponse(tank_serializer.data, status=status.HTTP_201_CREATED) 
   #return JsonResponse(tank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   #return HttpResponse ('Done')

@csrf_exempt
def createlogin(request):
   print("in updateLogin")
   login_data = JSONParser().parse(request)
   print(login_data)
   login_serializer = LoginSerializer(data=login_data)
   
   if login_serializer.is_valid():
      login_serializer.save() # data base saved
      return JsonResponse(login_serializer.data, status=status.HTTP_201_CREATED) 
   return JsonResponse(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)