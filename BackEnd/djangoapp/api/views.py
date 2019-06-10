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
import random
from datetime import datetime
from .models import Tanks_Overall_Status, Tank, Quality_Avg,Output_Parameter_UserDefined
from .models import Input_Parameter_ProfitMax, Plant_Constraints, New_Naphtha, Output_Comparision
from .models import Output_Parameter_Running, Output_Parameter_ProfitMax, Receipt_Tank
from .models import  Input_Parameter_BestFit, Input_Parameter_UserDefined, New_Naphtha_Quality_Supplier
from .models import Naphtha_Plan_All_Months, Naphtha_Plan_Single_Month,Output_Parameter_BestFit
from .models import Quality_Real, Input_Parameter_Running, Next_Hour_Selection,Quality_NIR_Actual,Quality_NIR_Pred, New_Naphtha_Quality_Lab
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
      if tankno == '0':
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            avg_quality =[]
            for i in range(1,6):
                  tank = Tank.objects.filter(tanks_Overall_Status = parent_obj,Tank_No = i).get()
                  quality_avg = Quality_Avg.objects.filter(tank = tank)
                  quality_avg =  list(quality_avg.values()) 
                  quality_avg = list(quality_avg[0].values())

                  avg_quality.append(quality_avg)

            return JsonResponse(avg_quality , safe = False, status=status.HTTP_201_CREATED)

            
      else:

            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = tankno).get()
            quality_avg = Quality_Avg.objects.filter(tank = tank)

            quality_avg = list(quality_avg.values())
            
            print ("*****************" + str(quality_avg[0]) + "******************")

            return JsonResponse(quality_avg[0] , safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getQualityReal(request, tankno):
     
      if tankno == '0':
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            print("##############################################################################")
           
            real_quality =[]
            for i in range(1,6):
                  tank = Tank.objects.filter(tanks_Overall_Status = parent_obj,Tank_No = i).get()
                  quality_real = Quality_Real.objects.filter(tank = tank)
                  quality_real =  list(quality_real.values()) 
                  quality_real = list(quality_real[0].values())

                  real_quality.append(quality_real)

            return JsonResponse(real_quality , safe = False, status=status.HTTP_201_CREATED)

            
      else:

      
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
      obj = {'suctiontank' : None, 'blendingtank' : None, 'blendratio' : None,'naphthaload' : None,
      'lpg' : None , 'c5' : None,'c6'  : None, 'heater': None, 'cot' : None, 'pdi' : None, 
      'pressure': None, 'paraffin': None,'olefins': None,'aromatics': None,
      'naphthene' : None,'inipratio' : None, 'density' : None,'ibp' : None,'fbp': None }
      if nexthourinput.U_D == True:
            parent_obj= Tanks_Overall_Status.objects.all().order_by('-id')[0]
            userdefinedinput = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj, Confirmation = True).get()
      
            obj['suctiontank'] = userdefinedinput.Suction_Tank_No_UD
            obj['blendingtank'] = userdefinedinput.Blending_Tank_No_UD
            obj['blendratio'] = userdefinedinput.Blend_Ratio_UD
            obj['naphthaload'] = userdefinedinput.Naphtha_Load_UD
            obj['lpg'] = userdefinedinput.LPG_Load_UD
            obj['c5'] = userdefinedinput.C5_Load_UD
            obj['c6'] = userdefinedinput.C6_Load_UD
            obj['heater'] = userdefinedinput.Naphtha_Heater_UD
            obj['cot'] = userdefinedinput.COT_UD
            obj['pdi'] = userdefinedinput.GF_PDI_UD
            obj['pressure'] = userdefinedinput.Suc_Pressure_UD
            obj['paraffin'] = userdefinedinput.Paraffin_UD
            obj['olefins'] = userdefinedinput.Olefins_UD
            obj['aromatics'] = userdefinedinput.Aromatics_UD
            obj['naphthene'] = userdefinedinput.Naphthene_UD
            obj['inipratio'] = userdefinedinput.IN_IP_Ratio_UD
            obj['density'] = userdefinedinput.Density_UD
            obj['ibp'] = userdefinedinput.IBP_UD
            obj['fbp'] = userdefinedinput.FBP_UD


            print("754345743644444444444444444444444444444444777777777777777729")
            #obj = list(obj.values())
            print(obj)
           
            

            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)

      if nexthourinput.B_F == True:
            tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            parent_obj = Plant_Constraints.objects.filter(tanks_Overall_Status = tankoverall).get()
      
            userdefinedinput = Input_Parameter_BestFit.objects.filter(plant_Constraints = parent_obj).get()

            obj['suctiontank'] = userdefinedinput.Suction_Tank_No_BF
            obj['blendingtank'] = userdefinedinput.Blending_Tank_No_BF
            obj['blendratio'] = userdefinedinput.Blend_Ratio_BF
            obj['naphthaload'] = userdefinedinput.Naphtha_Load_BF
            obj['lpg'] = userdefinedinput.LPG_Load_BF
            obj['c5'] = userdefinedinput.C5_Load_BF
            obj['c6'] = userdefinedinput.C6_Load_BF
            obj['heater'] = userdefinedinput.Naphtha_Heater_BF
            obj['cot'] = userdefinedinput.COT_BF
            obj['pdi'] = userdefinedinput.GF_PDI_BF
            obj['pressure'] = userdefinedinput.Suc_Pressure_BF
            obj['paraffin'] = userdefinedinput.Paraffin_BF
            obj['olefins'] = userdefinedinput.Olefins_BF
            obj['aromatics'] = userdefinedinput.Aromatics_BF
            obj['naphthene'] = userdefinedinput.Naphthene_BF
            obj['inipratio'] = userdefinedinput.IN_IP_Ratio_BF
            obj['density'] = userdefinedinput.Density_BF
            obj['ibp'] = userdefinedinput.IBP_BF
            obj['fbp'] = userdefinedinput.FBP_BF
        
            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)


            
            
      if nexthourinput.P_M == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            userdefinedinput = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()

            obj['suctiontank'] = userdefinedinput.Suction_Tank_No_PM
            obj['blendingtank'] = userdefinedinput.Blending_Tank_No_PM
            obj['blendratio'] = userdefinedinput.Blend_Ratio_PM
            obj['naphthaload'] = userdefinedinput.Naphtha_Load_PM
            obj['lpg'] = userdefinedinput.LPG_Load_PM
            obj['c5'] = userdefinedinput.C5_Load_PM
            obj['c6'] = userdefinedinput.C6_Load_PM
            obj['heater'] = userdefinedinput.Naphtha_Heater_PM
            obj['cot'] = userdefinedinput.COT_PM
            obj['pdi'] = userdefinedinput.GF_PDI_PM
            obj['pressure'] = userdefinedinput.Suc_Pressure_PM
            obj['paraffin'] = userdefinedinput.Paraffin_PM
            obj['olefins'] = userdefinedinput.Olefins_PM
            obj['aromatics'] = userdefinedinput.Aromatics_PM
            obj['naphthene'] = userdefinedinput.Naphthene_PM
            obj['inipratio'] = userdefinedinput.IN_IP_Ratio_PM
            obj['density'] = userdefinedinput.Density_PM
            obj['ibp'] = userdefinedinput.IBP_PM
            obj['fbp'] = userdefinedinput.FBP_PM
        
            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)

      if nexthourinput.R_N == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            userdefinedinput = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj).get()

            obj['suctiontank'] = parent_obj.Suction_Tank_No_RN
            obj['blendingtank'] = parent_obj.Blending_Tank_No_RN
            obj['blendratio'] = parent_obj.Blend_Ratio_RN
            obj['naphthaload'] = userdefinedinput.Naphtha_Load_RN
            obj['lpg'] = userdefinedinput.LPG_Load_RN
            obj['c5'] = userdefinedinput.C5_Load_RN
            obj['c6'] = userdefinedinput.C6_Load_RN
            obj['heater'] = userdefinedinput.Naphtha_Heater_RN
            obj['cot'] = userdefinedinput.COT_RN
            obj['pdi'] = userdefinedinput.GF_PDI_RN
            obj['pressure'] = userdefinedinput.Suc_Pressure_RN
            obj['paraffin'] = userdefinedinput.Paraffin_RN
            obj['olefins'] = userdefinedinput.Olefins_RN
            obj['aromatics'] = userdefinedinput.Aromatics_RN
            obj['naphthene'] = userdefinedinput.Naphthene_RN
            obj['inipratio'] = userdefinedinput.IN_IP_Ratio_RN
            obj['density'] = userdefinedinput.Density_RN
            obj['ibp'] = userdefinedinput.IBP_RN
            obj['fbp'] = userdefinedinput.FBP_RN
        
            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)

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
def getUserDefinedOutput(request):
      
      udinput = Input_Parameter_UserDefined.objects.all().order_by('-id')[0]
      
      udoutput = Output_Parameter_UserDefined.objects.filter(input_Parameter_UserDefined = udinput)

      udoutput = list(udoutput.values())


      return JsonResponse(udoutput[0], safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getRunningOutput(request):
      
      rninput = Input_Parameter_Running.objects.all().order_by('-id')[0]
      
      rnoutput = Output_Parameter_Running.objects.filter(input_Parameter_Running = rninput)

      rnoutput = list(rnoutput.values())


      return JsonResponse(rnoutput[0], safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getProfiitMaxOutput(request):
      
      pminput = Input_Parameter_ProfitMax.objects.all().order_by('-id')[0]
      
      pmoutput = Output_Parameter_ProfitMax.objects.filter(input_Parameter_ProfitMax = pminput)

      pmoutput = list(pmoutput.values())


      return JsonResponse(pmoutput[0], safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getBestFitOutput(request):
      
      bfinput = Input_Parameter_BestFit.objects.all().order_by('-id')[0]
      
      bfoutput = Output_Parameter_BestFit.objects.filter(input_Parameter_BestFit = bfinput)

      bfoutput = list(bfoutput.values())


      return JsonResponse(bfoutput[0], safe = False, status=status.HTTP_201_CREATED)


  
@csrf_exempt
def getNextHourOutput(request):
      
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      nexthouroutput = Next_Hour_Selection.objects.filter(tanks_Overall_Status = parent_obj).get()

      if nexthouroutput.U_D == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            userdefineinput = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj, Confirmation = True).get()
            userdefineoutput = Output_Parameter_UserDefined.objects.filter(input_Parameter_UserDefined = userdefineinput)

            userdefineoutput = list(userdefineoutput.values())
            user = userdefineoutput[0]
            obj = list(user.values())
            

            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)

      if nexthouroutput.B_F == True:
            tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            parent_obj = Plant_Constraints.objects.filter(tanks_Overall_Status = tankoverall).get()
      
            bestfitinput = Input_Parameter_BestFit.objects.filter(plant_Constraints = parent_obj).get()
            bestfitoutput = Output_Parameter_BestFit.objects.filter(input_Parameter_BestFit = bestfitinput)

            bestfitoutput = list(bestfitoutput.values())
            user = bestfitoutput[0]
            obj = list(user.values())
            

            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)
            
      if nexthouroutput.P_M == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            profitmaxinput = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()
            profitmaxoutput = Output_Parameter_ProfitMax.objects.filter(input_Parameter_ProfitMax = profitmaxinput)

            profitmaxoutput = list(profitmaxoutput.values())
            user = profitmaxoutput[0]
            obj = list(user.values())
            

            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)

      if nexthouroutput.R_N == True:
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            runninginput = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj).get()
            nexthouroutput = Output_Parameter_Running.objects.filter(input_Parameter_Running = runninginput)

            nexthouroutput = list(nexthouroutput.values())
            user = nexthouroutput[0]
            obj = list(user.values())
            

            return JsonResponse(obj , safe = False, status=status.HTTP_201_CREATED)


@csrf_exempt
def updateNextHourSelection(request, selection):
      parent_obj = Next_Hour_Selection.objects.all().order_by('-id')[0]
      if selection == 'bestfit':
            Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = False, B_F = True, P_M = False, R_N = False)
      
      if selection == 'profitmax':
            Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = False, B_F = False, P_M = True, R_N = False)
      
      if selection == 'running':
            Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = False, B_F = False, P_M = False, R_N = True)
      
      if selection == 'userdefined':
            parent_obj = Input_Parameter_UserDefined.objects.all().order_by('-id')[0]
            tank_ids = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj.tanks_Overall_Status)
            for i in range(0, len(tank_ids)):
                  Input_Parameter_UserDefined.objects.filter(pk=tank_ids[i].id).update(Confirmation = False)
                 
            obj = Input_Parameter_UserDefined.objects.filter(pk=parent_obj.id).get()
            obj.Confirmation = True 
            obj.save()
            #parent_obj = Next_Hour_Selection.objects.all().order_by('-id')[0]
            #Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = True, B_F = False, P_M = False, R_N = False)

      return JsonResponse(1, safe = False, status=status.HTTP_201_CREATED)


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

@csrf_exempt
def getThisMonthDetail(request):
      
      parent = New_Naphtha.objects.all().order_by('-id')
      currentmonth = datetime.strptime(parent[0].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").month
      currentyear = datetime.strptime(parent[0].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").year
      array = []

      for i in range(0,len(parent)):
            M = datetime.strptime(parent[i].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").month
            Y = datetime.strptime(parent[i].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").year
            if M == currentmonth and Y == currentyear:
                  obj = New_Naphtha.objects.filter(pk = parent[i].id)
                  array.append(list(obj.values()))

      return JsonResponse(array, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getAnyMonthDetail(request, fromdate, todate):


      fromdate = datetime.strptime(fromdate, "%Y-%m-%d")
      todate = datetime.strptime(todate, "%Y-%m-%d")

      frommonth = fromdate.month
      fromyear = fromdate.year
      tomonth = todate.month
      toyear = todate.year
      
      array = New_Naphtha.objects.all()

      plan = []

      for i in range(0,len(array)):
            M = datetime.strptime(array[i].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").month
            Y = datetime.strptime(array[i].Date_Transfer_From.strftime("%Y-%m-%d"), "%Y-%m-%d").year
            if M >= frommonth and Y >= fromyear and M <= tomonth and Y <= toyear:
                  arraymonth = New_Naphtha.objects.filter(pk = array[i].id)
                 # for k in range(0,len(arraymonth)):
                  plan.append(list(arraymonth.values()))
                  
      
      return JsonResponse(plan, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def postNaphthaMonthPlan(request):

      data = JSONParser().parse(request)
      #date = data['Date'].strftime("%Y-%m-%d")
      date = datetime.strptime(data['Date'], "%Y-%m-%d")
      Naphtha_Plan_Single_Month.objects.create(Date = date,
                                                 Total_Stock = data['Total_Stock'], 
                                                 Usable_Stock = data['Usable_Stock'],
                                                 Source = data['Source'], 
                                                 Quantity = data['Quantity'],
                                                 Actual_NCU_TPH = data['Actual_NCU_TPH'], Budget_NCU_TPH = data['Budget_NCU_TPH'], 
                                                 Actual_CPP_TPD = data['Actual_CPP_TPD'] ,
                                                 Budget_CPP_TPD = data['Budget_CPP_TPD'], Draft_Level = data['Draft_Level'] )


      return JsonResponse(1, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def PostNewNaphthaDetails(request):

      data = JSONParser().parse(request)
      #date = data['Date'].strftime("%Y-%m-%d")
      parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
      
      Date_Transfer_From = datetime.strptime(data['Date_Transfer_From'], "%Y-%m-%d")
      Date_Transfer_To = datetime.strptime(data['Date_Transfer_To'], "%Y-%m-%d")
      New_Naphtha.objects.create(Transport_Type = data['Transport_Type'], 
                                 Date_Transfer_From = Date_Transfer_From,
                                 Date_Transfer_To = Date_Transfer_To, 
                                 HOJ = data['HOJ'],
                                 Load_Port = data['Load_Port'], BL_Quantity = data['BL_Quantity'], 
                                 Shore_Quantity = data['Shore_Quantity'] , Shortage_Quantity = data['BL_Quantity']-data['Shore_Quantity'],
                                 Opening_Stock = data['Opening_Stock'], Source = data['Source'],
                                 PCN_NCU = data['PCN_NCU'], PCN_CPP = data['PCN_CPP'],
                                 FGN_CPP = data['FGN_CPP'], CBFS_CPP = data['CBFS_CPP'], Vessel_Name = data['Vessel_Name'],
                                 tanks_Overall_Status = parent_obj)
      obj = New_Naphtha.objects.all().order_by('-id')[0]

      New_Naphtha_Quality_Supplier.objects.create(Aromatics = data['Aromatics'], 
                                 Colour = data['Colour'],
                                 Density = data['Density'], 
                                 IN_IP_Ratio = data['IN_IP_Ratio'],
                                 Naphthene = data['Naphthene'], Olefins = data['Olefins'], 
                                 Paraffin = data['Paraffin'] ,
                                 RVP = data['RVP'], Sulfur = data['Sulfur'],
                                 FBP = data['FBP'], IBP = data['IBP'], new_Naphtha = obj)


      New_Naphtha_Quality_Lab.objects.create(Aromatics = random.randint(10,100), 
                              Colour = random.randint(10,100),
                              Density = random.randint(10,100), 
                              IN_IP_Ratio = random.randint(10,50),
                              Naphthene = random.randint(10,50), Olefins = random.randint(10,50), 
                              Paraffin = random.randint(10,50) ,
                              RVP = random.randint(10,50), Sulfur = random.randint(10,50),
                              FBP = random.randint(10,50), IBP = random.randint(10,50), new_Naphtha = obj)


      Receipt_Tank.objects.create(Tank_No_1 = 0, Tank_No_1_Receiving = -1,
                              Tank_No_2 = 0, Tank_No_2_Receiving = -1,Tank_No_3 = 0, Tank_No_3_Receiving = -1,
                              Tank_No_4 = 0, Tank_No_4_Receiving = -1,Tank_No_5 = 0, Tank_No_5_Receiving = -1,
                               new_Naphtha = obj)


      return JsonResponse(1, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def GetReceivedNaphtha(request):
      
      parent_obj = New_Naphtha.objects.all().order_by('-id')[0]
      suppliedquality = New_Naphtha_Quality_Supplier.objects.filter(new_Naphtha = parent_obj)
      labquality = New_Naphtha_Quality_Lab.objects.filter(new_Naphtha = parent_obj)
      parent_obj = New_Naphtha.objects.filter(pk=parent_obj.id)

      received = []
      suppliedquality =  list(suppliedquality.values()) 
      suppliedquality = list(suppliedquality[0].values())    
      labquality =  list(labquality.values()) 
      labquality = list(labquality[0].values()) 
      parent_obj =  list(parent_obj.values()) 
      parent_obj = list(parent_obj[0].values()) 

      received.append(parent_obj)
      received.append(suppliedquality)
      received.append(labquality)

      return JsonResponse(received , safe = False, status=status.HTTP_201_CREATED)


@csrf_exempt
def transferNaphthaQuantity(request):
      data = JSONParser().parse(request)
      parent_obj = Receipt_Tank.objects.all().order_by('-id')[0]

      tanknoreceiving = [0] * 5
      for i in range(0,5):

            if data[i] == 0:
                  tanknoreceiving[i] = -1
            else:
                  if i+1 == data[5]:
                        tanknoreceiving[i] = 0
                  else:
                        tanknoreceiving[i] = 1


      parent_obj.Tank_No_1 = data[0]
      parent_obj.Tank_No_2 = data[1]  
      parent_obj.Tank_No_3 = data[2]
      parent_obj.Tank_No_4 = data[3]
      parent_obj.Tank_No_5 = data[4]
      parent_obj.Tank_No_1_Receiving = tanknoreceiving[0]
      parent_obj.Tank_No_2_Receiving = tanknoreceiving[1]
      parent_obj.Tank_No_3_Receiving = tanknoreceiving[2]
      parent_obj.Tank_No_4_Receiving = tanknoreceiving[3]
      parent_obj.Tank_No_5_Receiving = tanknoreceiving[4]   

      parent_obj.save()

      return JsonResponse(1, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getInputOutput(request, fromdate, todate):


      fromdate = datetime.strptime(fromdate, "%Y-%m-%d")
      todate = datetime.strptime(todate, "%Y-%m-%d")

      fromday = fromdate.day
      frommonth = fromdate.month
      fromyear = fromdate.year
      today = todate.day
      tomonth = todate.month
      toyear = todate.year

      
      array = Tanks_Overall_Status.objects.all()
    
      inputoutput = []

      for i in range(0,len(array)):

            D = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").day
            M = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").month
            Y = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").year
           
            if D >= fromday and M >= frommonth and Y >= fromyear and D <= today and M <= tomonth and Y <= toyear:
                  
                  Input = Input_Parameter_Running.objects.filter(tanks_Overall_Status = array[i]).get()
                  Output = Output_Parameter_Running.objects.filter(input_Parameter_Running = Input).get()
                  Comparison = Output_Comparision.objects.filter(output_Parameter_Running = Output) 
           
                  inputoutput.append(list(Comparison.values())[0])
                  
      
      return JsonResponse(inputoutput, safe = False, status=status.HTTP_201_CREATED)

@csrf_exempt
def getQualityQuantity(request, fromdate, todate):


      fromdate = datetime.strptime(fromdate, "%Y-%m-%d")
      todate = datetime.strptime(todate, "%Y-%m-%d")

      frommonth = fromdate.month
      fromyear = fromdate.year
      tomonth = todate.month
      toyear = todate.year
      
      array = Tanks_Overall_Status.objects.all().order_by('id')
 
      qualityquantity = []
     
      for i in range(0,len(array)):

            M = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").month
            Y = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").year
           
            if M >= frommonth and Y >= fromyear and M <= tomonth and Y <= toyear:

                  dayobjday = datetime.strptime(array[i].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").day

                  flag = False

                  for f in range(0,len(qualityquantity)):
                        thisdayinlist = datetime.strptime(qualityquantity[f][0], "%Y-%m-%d").day
                        thismonthinlist = datetime.strptime(qualityquantity[f][0], "%Y-%m-%d").month
                        thisyearinlist = datetime.strptime(qualityquantity[f][0], "%Y-%m-%d").year
                        if thisdayinlist == dayobjday and thismonthinlist == M and thisyearinlist == Y:
                              flag = True

                  if not flag:

                        temparray = []

                        for j in range(0,len(array)):

                              thisday = datetime.strptime(array[j].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").day
                              thismonth = datetime.strptime(array[j].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").month
                              thisyear = datetime.strptime(array[j].Date_Time.strftime("%Y-%m-%d"), "%Y-%m-%d").year

                              if dayobjday == thisday and M == thismonth and Y == thisyear:

                                    temparray.append(array[j])
                              
                        tankweights = []
                        tankquality = []
                        tankconsumption = []
                        tankreceipt = []
                        dayreport = []

                        for k in range(0,5):

                              tankobj = Tank.objects.filter(tanks_Overall_Status = temparray[-1], Tank_No = k+1).get()
                              tankweights.append(tankobj.Weight)
                              quality = Quality_Avg.objects.filter(tank = tankobj)
                              tankquality.append(list(quality.values())[0])

                              if len(qualityquantity):
                                    
                                    weightdiff = tankobj.Weight - qualityquantity[-1][1][k]

                                    if weightdiff > 0:
                                          tankreceipt.append(weightdiff)
                                          tankconsumption.append(0)
                                    else:
                                          tankconsumption.append(-1 * weightdiff)
                                          tankreceipt.append(0)
                              else:
                                    tankreceipt.append(0)
                                    tankconsumption.append(0)              
                                    
                        dayreport.append(temparray[-1].Date_Time.strftime("%Y-%m-%d"))                    
                        dayreport.append(tankweights)
                        dayreport.append(tankconsumption)
                        dayreport.append(tankreceipt)
                        dayreport.append(tankquality)

                        qualityquantity.append(dayreport)
                  
            
                  
      
      return JsonResponse(qualityquantity, safe = False, status=status.HTTP_201_CREATED)      
