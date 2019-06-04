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
from .models import Input_Parameter_ProfitMax, Plant_Constraints
from .models import  Input_Parameter_BestFit, Input_Parameter_UserDefined
from .models import Naphtha_Plan_All_Months, Naphtha_Plan_Single_Month
from .models import Quality_Real, Input_Parameter_Running, Next_Hour_Selection,Quality_NIR_Actual,Quality_NIR_Pred
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
def postUserDefinedInputs(request):
      data = JSONParser().parse(request)
      #Input_Parameter_UserDefined.save(data = data)
      print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***********~~~~~~~~~~~~~~~~~~~~~*")
      Input_Parameter_UserDefined.objects.create(Suction_Tank_No_UD = data['Suction_Tank_No_UD'],
                                                 Blending_Tank_No_UD = data['Blending_Tank_No_UD'], 
                                                 Blend_Ratio_UD = data['Blend_Ratio_UD'],
                                                 Naphtha_Load_UD = data['Naphtha_Load_UD'], 
                                                 LPG_Load_UD = data['LPG_Load_UD'],
                                                 C5_Load_UD = data['C5_Load_UD'], C6_Load_UD = data['C6_Load_UD'], 
                                                 Naphtha_Heater_UD = data['Naphtha_Heater_UD'] ,
                                                 COT_UD = data['COT_UD'], GF_PDI_UD = data['GF_PDI_UD'], 
                                                 Suc_Pressure_UD = data['Suc_Pressure_UD'] )
      return JsonResponse(1, safe = False, status=status.HTTP_201_CREATED)


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
def getRunningInput(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      obj = Tanks_Overall_Status.objects.all().order_by('-id')
      runninginput = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj)

      runninginput = list(runninginput.values())
      obj = list(obj.values())
      array = []
      array.append(runninginput[0])
      array.append(obj[0])
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(array, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getProfitMaxInput(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      profitmaxinput = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj)

      profitmaxinput = list(profitmaxinput.values())
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(profitmaxinput[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getBestFitInput(request):

      tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      parent_obj = Plant_Constraints.objects.filter(tanks_Overall_Status = tankoverall).get()
      
      bestfitinput = Input_Parameter_BestFit.objects.filter(plant_Constraints = parent_obj)

      bestfitinput = list(bestfitinput.values())
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(bestfitinput[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getNextHourInput(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      nexthourinput = Next_Hour_Selection.objects.filter(tanks_Overall_Status = parent_obj).get()
      if nexthourinput.U_D == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            userdefinedinput = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj, Confirmation = True)

            userdefinedinput = list(userdefinedinput.values())

            return JsonResponse(userdefinedinput[0] , safe = False, status=status.HTTP_201_CREATED)

      if nexthourinput.B_F == True:
            tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            parent_obj = Plant_Constraints.objects.filter(tanks_Overall_Status = tankoverall).get()
      
            bestfitinput = Input_Parameter_BestFit.objects.filter(plant_Constraints = parent_obj)

            bestfitinput = list(bestfitinput.values())


            return JsonResponse(bestfitinput[0] , safe = False, status=status.HTTP_201_CREATED)
            
      if nexthourinput.P_M == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            profitmaxinput = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj)

            profitmaxinput = list(profitmaxinput.values())


            return JsonResponse(profitmaxinput[0] , safe = False, status=status.HTTP_201_CREATED)

      if nexthourinput.R_N == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            runninginput = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj)

            runninginput = list(runninginput.values())

            return JsonResponse(runninginput[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getNirActual(request):

      tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      
      niractual = Quality_NIR_Actual.objects.filter(tanks_Overall_Status = tankoverall)

      niractual = list(niractual.values())
      
      #print ("*****************" + str(quality_avg[0]) + "******************")

      return JsonResponse(niractual[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getNirModel(request):
      
      tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      
      nirmodel = Quality_NIR_Pred.objects.filter(tanks_Overall_Status = tankoverall)

      nirmodel = list(nirmodel.values())


      return JsonResponse(nirmodel[0], safe = False, status=status.HTTP_201_CREATED)

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