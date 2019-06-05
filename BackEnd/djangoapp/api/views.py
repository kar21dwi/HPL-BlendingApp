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
from .models import Tanks_Overall_Status, Tank, Quality_Avg,Output_Parameter_UserDefined
from .models import Input_Parameter_ProfitMax, Plant_Constraints
from .models import Output_Parameter_Running, Output_Parameter_ProfitMax
from .models import  Input_Parameter_BestFit, Input_Parameter_UserDefined
from .models import Naphtha_Plan_All_Months, Naphtha_Plan_Single_Month,Output_Parameter_BestFit
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
            Input_Parameter_UserDefined.objects.filter(pk=parent_obj.id).update(Confirmation = True)
            parent_obj = Next_Hour_Selection.objects.all().order_by('-id')[0]
            Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = True, B_F = False, P_M = False, R_N = False)

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