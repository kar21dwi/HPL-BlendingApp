from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints, Output_Parameter_Running, Output_Comparision
from djangoapp.api.models import Quality_NIR_Pred, Next_Hour_Selection, Input_Parameter_BestFit, Input_Parameter_UserDefined, Output_Parameter_UserDefined, Naphtha_Plan_Single_Month, Naphtha_Plan_All_Months
from djangoapp.api.models import Output_Parameter_BestFit, Input_Parameter_ProfitMax, Quality_Real,Output_Parameter_ProfitMax, Input_Parameter_Running, Model_Output_Parameter_Running, Naphtha_Plan_Summary
from djangoapp.dlmodels.qualityreal import Quality_Real_Model
from djangoapp.dlmodels.bestfit import Best_Fit_Model
from djangoapp.dlmodels.runningmodeloutput import Running_Model_Output
from djangoapp.dlmodels.profitmax import Profit_Max_Model
from djangoapp.dlmodels.userdefined import User_Defined_Model
import numpy
import random
import datetime


#create all signals

#signals
@receiver(post_save, sender=Tanks_Overall_Status)
def update_tank_overall(sender, instance, **kwargs):

   old_obj_next_hr = Next_Hour_Selection.objects.all().order_by('-id')[0]
   parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[1]
   
   if old_obj_next_hr.U_D == True:
        userdefined = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj , Confirmation = True).get()

        Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = userdefined.Suction_Tank_No_UD,
                                            Blending_Tank_No_RN = userdefined.Blending_Tank_No_UD, 
                                            Blend_Ratio_RN = userdefined.Blend_Ratio_UD)       
        
   if old_obj_next_hr.B_F == True:
       bestfit = Input_Parameter_BestFit.objects.filter(plant_Constraints = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()).get()

       Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = bestfit.Suction_Tank_No_BF,
                                             Blending_Tank_No_RN = bestfit.Blending_Tank_No_BF, 
                                             Blend_Ratio_RN = bestfit.Blend_Ratio_BF)  
                                            
   if old_obj_next_hr.P_M == True:
        profitmax = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()

        Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = profitmax.Suction_Tank_No_PM,
                                            Blending_Tank_No_RN = profitmax.Blending_Tank_No_PM, 
                                            Blend_Ratio_RN = profitmax.Blend_Ratio_PM)       

   if old_obj_next_hr.R_N == True:
        
        Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = parent_obj.Suction_Tank_No_RN,
                                            Blending_Tank_No_RN = parent_obj.Blending_Tank_No_RN, 
                                            Blend_Ratio_RN = parent_obj.Blend_Ratio_RN)   
       

#Signals for Tanks Overall Status
@receiver(post_save, sender=Tanks_Overall_Status)
def save_tank(sender, instance, **kwargs):

    #print ("***************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************")
    #print ("inside save_tank")
    #print ("****************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$****************************")
    old_obj = Tanks_Overall_Status.objects.all().order_by('-id')[1]
    suctiontank = old_obj.Suction_Tank_No_RN
    blendingtank = old_obj.Blending_Tank_No_RN    
    #print ("********************************************")
    #print (Receipt_Tank.objects.filter(Tank_No_2_Receiving = 0).exists())
    #print ("********************************************")

    receving_tank = [0] * 5
    newnaphtha = [0] * 5

    if(Receipt_Tank.objects.filter(Tank_No_1_Receiving = 0).exists()):
        receving_tank[0] = 1
        newnaphtha[0] = Receipt_Tank.objects.filter(Tank_No_1_Receiving = 0).get().new_Naphtha
    else:
        receving_tank[0] = 0

    if(Receipt_Tank.objects.filter(Tank_No_2_Receiving = 0).exists()):
        receving_tank[1] = 1
        newnaphtha[1] = Receipt_Tank.objects.filter(Tank_No_2_Receiving = 0).get().new_Naphtha   
    else:
        receving_tank[1] = 0    

    if(Receipt_Tank.objects.filter(Tank_No_3_Receiving = 0).exists()):
        receving_tank[2] = 1
        newnaphtha[2] = Receipt_Tank.objects.filter(Tank_No_3_Receiving = 0).get().new_Naphtha
    else:
       receving_tank[2] = 0

    if(Receipt_Tank.objects.filter(Tank_No_4_Receiving = 0).exists()):
        receving_tank[3] = 1
        newnaphtha[3] = Receipt_Tank.objects.filter(Tank_No_4_Receiving = 0).get().new_Naphtha
    else:
       receving_tank[3] = 0
    
    if(Receipt_Tank.objects.filter(Tank_No_5_Receiving = 0).exists()):
        receving_tank[4] = 1
        newnaphtha[4] = Receipt_Tank.objects.filter(Tank_No_5_Receiving = 0).get().new_Naphtha
    else:
        receving_tank[4] = 0

    for i in range(0,5):

        old_tank = Tank.objects.filter(tanks_Overall_Status = old_obj , Tank_No=i+1).get()
        old_level = old_tank.Level

        old_density_quaity_avg = Quality_Avg.objects.filter(tank= old_tank).get().Density

        if receving_tank[i] == 1 and (suctiontank!=i+1 or blendingtank!=i+1):
            #print('*************************')
            #print(receving_tank[i])
            #print('**********************')
            new_level = old_level + 500
            receiving = True
        else:
            receiving = False
            if  suctiontank==i+1 or blendingtank==i+1:
               new_level = old_level - 100            
            else:
               new_level = old_level     

        Tank.objects.create(Level = new_level, Receiving_Naphtha = receiving, Tank_No =i+1,
                            tanks_Overall_Status= instance)
     

        
    
#Signals for the Quality Avg Class

@receiver(post_save, sender=Tank)
def save_avg_quality(sender, instance, **kwargs):
    
    old_obj_tankoverallstatus = Tanks_Overall_Status.objects.all().order_by('-id')[1]
    old_obj_tank = Tank.objects.filter(tanks_Overall_Status=old_obj_tankoverallstatus,Tank_No = instance.Tank_No).get()
    old_obj_qualityavg = Quality_Avg.objects.filter(tank=old_obj_tank).get()

    if instance.Receiving_Naphtha == True:
        if instance.Tank_No == 1:
           newnaphtha = Receipt_Tank.objects.filter(Tank_No_1_Receiving = 0).get().new_Naphtha
        if instance.Tank_No == 2:
            newnaphtha = Receipt_Tank.objects.filter(Tank_No_2_Receiving = 0).get().new_Naphtha
        if instance.Tank_No == 3:
            newnaphtha = Receipt_Tank.objects.filter(Tank_No_3_Receiving = 0).get().new_Naphtha
        if instance.Tank_No == 4:
            newnaphtha = Receipt_Tank.objects.filter(Tank_No_4_Receiving = 0).get().new_Naphtha
        if instance.Tank_No == 5:
            newnaphtha = Receipt_Tank.objects.filter(Tank_No_5_Receiving = 0).get().new_Naphtha

        newnaphthaquaity = New_Naphtha_Quality_Lab.objects.filter(new_Naphtha = newnaphtha).get()

        paraffinnew = round((old_obj_qualityavg.Paraffin*old_obj_tank.Level + newnaphthaquaity.Paraffin* (instance.Level-old_obj_tank.Level))/instance.Level , 2)
        olefinsnnew = round((old_obj_qualityavg.Olefins*old_obj_tank.Level + newnaphthaquaity.Olefins* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        aromaticsnnew = round((old_obj_qualityavg.Aromatics*old_obj_tank.Level + newnaphthaquaity.Aromatics* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        naphthenenew = round((old_obj_qualityavg.Naphthene*old_obj_tank.Level + newnaphthaquaity.Naphthene* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        iniprationew = round((old_obj_qualityavg.IN_IP_Ratio*old_obj_tank.Level + newnaphthaquaity.IN_IP_Ratio* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        densitynew = round((old_obj_qualityavg.Density*old_obj_tank.Level + newnaphthaquaity.Density* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        ibpnew = round((old_obj_qualityavg.IBP*old_obj_tank.Level + newnaphthaquaity.IBP* (instance.Level-old_obj_tank.Level))/instance.Level, 2)
        fbpnew = round((old_obj_qualityavg.FBP*old_obj_tank.Level + newnaphthaquaity.FBP* (instance.Level-old_obj_tank.Level))/instance.Level, 2)
        sulfurnew = round((old_obj_qualityavg.Sulfur*old_obj_tank.Level + newnaphthaquaity.Sulfur* (instance.Level-old_obj_tank.Level))/instance.Level, 2)
        colournew = round((old_obj_qualityavg.Colour*old_obj_tank.Level + newnaphthaquaity.Colour* (instance.Level-old_obj_tank.Level))/instance.Level,2)
        rvpnew = round((old_obj_qualityavg.RVP*old_obj_tank.Level + newnaphthaquaity.RVP* (instance.Level-old_obj_tank.Level))/instance.Level, 2)

        Quality_Avg.objects.create(Paraffin = paraffinnew, Olefins = olefinsnnew, 
                                Aromatics = aromaticsnnew, Naphthene = naphthenenew, 
                                IN_IP_Ratio = iniprationew, Density = densitynew,
                                IBP = ibpnew, FBP = fbpnew, Sulfur = sulfurnew, 
                                Colour = colournew, RVP = rvpnew, 
                                tank = instance)
    else:
        Quality_Avg.objects.create(Paraffin = old_obj_qualityavg.Paraffin, Olefins = old_obj_qualityavg.Olefins, 
                                Aromatics = old_obj_qualityavg.Aromatics, Naphthene = old_obj_qualityavg.Naphthene, 
                                IN_IP_Ratio = old_obj_qualityavg.IN_IP_Ratio, Density = old_obj_qualityavg.Density,
                                IBP = old_obj_qualityavg.IBP, FBP = old_obj_qualityavg.IBP,Sulfur = old_obj_qualityavg.Sulfur, 
                                Colour = old_obj_qualityavg.Colour, RVP = old_obj_qualityavg.RVP, 
                                tank = instance)
 

 #Signals for the update weight
@receiver(post_save, sender=Quality_Avg)
def update_tank_weight(sender, instance, **kwargs):
    
    weight = instance.Density*( instance.tank.Level)*3.14*10.8*10.8*9.8

    Tank.objects.filter(pk=instance.tank.id).update(Weight = round(weight/1000 , 2))


#Signals for the Quality NIR Actual Class
@receiver(post_save, sender=Tanks_Overall_Status)
def save_nir_actual(sender, instance, **kwargs):
    
    old_obj_tankoverallstatus = Tanks_Overall_Status.objects.all().order_by('-id')[1]
    suctiontank = old_obj_tankoverallstatus.Suction_Tank_No_RN
    blendingtank = old_obj_tankoverallstatus.Blending_Tank_No_RN
    br = old_obj_tankoverallstatus.Blend_Ratio_RN

    old_obj_tank_s = Tank.objects.filter(tanks_Overall_Status=old_obj_tankoverallstatus,Tank_No = suctiontank).get()
    old_obj_tank_b = Tank.objects.filter(tanks_Overall_Status=old_obj_tankoverallstatus,Tank_No = blendingtank).get()
    old_obj_qualityavg_s = Quality_Avg.objects.filter(tank=old_obj_tank_s).get()
    old_obj_qualityavg_b = Quality_Avg.objects.filter(tank=old_obj_tank_b).get()

    nirparaffin = round(old_obj_qualityavg_s.Paraffin*br + old_obj_qualityavg_b.Paraffin*(1-br),2)
    niraromatics = round(old_obj_qualityavg_s.Aromatics*br + old_obj_qualityavg_b.Aromatics*(1-br), 2)
    nirdensity = round(old_obj_qualityavg_s.Density*br + old_obj_qualityavg_b.Density*(1-br), 2)
    nirinipratio = round(old_obj_qualityavg_s.IN_IP_Ratio*br + old_obj_qualityavg_b.IN_IP_Ratio*(1-br), 2)

    Quality_NIR_Actual.objects.create(Paraffin_NIR = nirparaffin, Aromatics_NIR = niraromatics, 
                                      IN_IP_Ratio_NIR = nirinipratio, Density_NIR = nirdensity, 
                                      tanks_Overall_Status = instance)


 #Signals for the Quality Real Class
@receiver(post_save, sender=Quality_Avg)
def save_quality_real(sender, instance, **kwargs):

    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
    childcount = len(Tank.objects.filter(tanks_Overall_Status=parent_obj))
    output = numpy.zeros((5, 4))
    if childcount == 5:
        output = Quality_Real_Model.quality_real_model(instance)

        for i in range(0,5):
            old_obj_tank = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = i+1).get()
    
            Quality_Real.objects.create(Paraffin_Real = output[i][0], Aromatics_Real = output[i][1], 
            Density_Real = output[i][2], IN_IP_Ratio_Real = output[i][3], tank = old_obj_tank)
           


#Signals for the Plant Constraints Class
@receiver(post_save, sender=Tanks_Overall_Status)
def save_plant_constraints(sender, instance, **kwargs):
    
   Plant_Constraints.objects.create(Max_Ethylene = 76, Max_Propylene = 40, Max_RPG = 60, Max_Benzene = 1.4,
                                    Max_C4_Mix = 22, Max_Fuel_Gas = 40, Max_BD = 1.9,
                                    tanks_Overall_Status = instance)

       
#Signals for the NIR Pred Class
@receiver(post_save, sender=Quality_Real)
def save_nir_pred(sender, instance, **kwargs):

    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
    suctiontank = parent_obj.Suction_Tank_No_RN
    blendingtank = parent_obj.Blending_Tank_No_RN
    br = parent_obj.Blend_Ratio_RN
    #print ("*************" + str(parent_obj) + "*************")

    childcount = 0
    tank_obj = Tank.objects.filter(tanks_Overall_Status = parent_obj)
    for i in range(0,5):
        if Quality_Real.objects.filter(tank = tank_obj[i]).exists():
            childcount = childcount + 1 

    if childcount == 5:
        tanksuction = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = suctiontank).get()
        #print("*************child count*****" + str(childcount) +"*******************")
        tankblending = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = blendingtank).get()
        #print("**********" + str(tankblending) +"*******************")
        realqualitysuction = Quality_Real.objects.filter(tank = tanksuction).get()
        #print("**********" + str(realqualitysuction) +"*******************")
        realqualityblending = Quality_Real.objects.filter(tank = tankblending).get()
        #print("**********" + str(realqualityblending) +"*******************")

        nirparaffin = round(realqualitysuction.Paraffin_Real*br + realqualityblending.Paraffin_Real*(1-br),2)
        niraromatics = round(realqualitysuction.Aromatics_Real*br + realqualityblending.Aromatics_Real*(1-br), 2)
        nirdensity = round(realqualitysuction.Density_Real*br + realqualityblending.Density_Real*(1-br), 2)
        nirinipratio = round(realqualitysuction.IN_IP_Ratio_Real*br + realqualityblending.IN_IP_Ratio_Real*(1-br), 2)

        #print ("************before nir pred create***************" + str(parent_obj))
        Quality_NIR_Pred.objects.create(Paraffin_NIR_Pred = nirparaffin, Aromatics_NIR_Pred = niraromatics, 
                                        IN_IP_Ratio_NIR_Pred = nirinipratio, Density_NIR_Pred = nirdensity, 
                                        tanks_Overall_Status = parent_obj)


#signals for the Next hour selection 
@receiver(post_save, sender = Tanks_Overall_Status)
def save_next_hr_selection(sender, instance, **kwargs):

    Next_Hour_Selection.objects.create(U_D = False, B_F = False, P_M = False, R_N =True, 
                                       tanks_Overall_Status = instance )


#Input Perameter for the Best_Fit Class
@receiver(post_save, sender = Plant_Constraints)
def save_best_fit_input(sender, instance, **kwargs):

    output = Best_Fit_Model.best_fit_model_recommendations(instance)
    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
    plantconstraints = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()

    Input_Parameter_BestFit.objects.create(Suction_Tank_No_BF = output[0], Blending_Tank_No_BF = output[1], Blend_Ratio_BF = output[2],IN_IP_Ratio_BF = output[3],
                                            Naphtha_Load_BF = output[4], LPG_Load_BF = output[5], C5_Load_BF = output[6], C6_Load_BF = output[7],
                                            Naphtha_Heater_BF = output[8],COT_BF = output[9],GF_PDI_BF = output[10],Suc_Pressure_BF = output[11],
                                            Paraffin_BF = output[12],Olefins_BF = output[13],Aromatics_BF = output[14],Naphthene_BF = output[15],
                                            Density_BF = output[16],IBP_BF = output[17],FBP_BF = output[18], 
                                            plant_Constraints = plantconstraints)


#Input Perameter for the Profit_Max Class
@receiver(post_save, sender = Tanks_Overall_Status)
def save_profit_max_input(sender, instance, **kwargs):

    output = Profit_Max_Model.profit_max_model_recommendations(instance)
    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
    
    Input_Parameter_ProfitMax.objects.create(Suction_Tank_No_PM = output[0], Blending_Tank_No_PM = output[1], Blend_Ratio_PM = output[2],IN_IP_Ratio_PM = output[3],
                                             Naphtha_Load_PM = output[4], LPG_Load_PM = output[5], C5_Load_PM = output[6], C6_Load_PM = output[7],
                                             Naphtha_Heater_PM = output[8],COT_PM = output[9],GF_PDI_PM = output[10],Suc_Pressure_PM = output[11],
                                             Paraffin_PM = output[12],Olefins_PM = output[13],Aromatics_PM = output[14],Naphthene_PM = output[15],
                                             Density_PM = output[16],IBP_PM = output[17],FBP_PM = output[18], 
                                             tanks_Overall_Status = parent_obj)




#Output Perameters for the Best_Fit Class
@receiver(post_save, sender = Input_Parameter_BestFit)
def save_best_fit_output(sender, instance, **kwargs):
    
    output = Best_Fit_Model.best_fit_model_output(instance)

    Output_Parameter_BestFit.objects.create(Ethylene_BF = output[0], Propylene_BF = output[1], RPG_BF = output[2], Benzene_BF = output[3],
                                            C4_Mix_BF = output[4], Fuel_Gas_BF = output[5], BD_BF = output[6],
                                            input_Parameter_BestFit = instance)    


#Output Perameters for the Profit_Max Class
@receiver(post_save, sender = Input_Parameter_ProfitMax)
def save_profit_max_output(sender, instance, **kwargs):

    output = Profit_Max_Model.profit_max_model_output(instance)

    Output_Parameter_ProfitMax.objects.create(Ethylene_PM = output[0], Propylene_PM = output[1], RPG_PM = output[2],
                                              Benzene_PM = output[3],C4_Mix_PM = output[4], Fuel_Gas_PM = output[5], BD_PM = output[6],
                                              input_Parameter_ProfitMax = instance)    


#Signals for the Input parameter userdDefine Class
@receiver(post_save, sender = Input_Parameter_UserDefined)
def save_user_defined_input(sender, instance, **kwargs):

    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
    suctiontank = instance.Suction_Tank_No_UD
    blendingtank = instance.Blending_Tank_No_UD
    br = instance.Blend_Ratio_UD
    tank_obj_s = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = suctiontank).get()
    tank_obj_b = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = blendingtank).get()

    tank_obj_s_qr = Quality_Real.objects.filter(tank = tank_obj_s).get()
    tank_obj_b_br = Quality_Real.objects.filter(tank = tank_obj_b).get()

    tank_obj_s_qa = Quality_Avg.objects.filter(tank = tank_obj_s).get()
    tank_obj_b_ba = Quality_Avg.objects.filter(tank = tank_obj_b).get()

    paraffin = tank_obj_s_qr.Paraffin_Real*br + tank_obj_b_br.Paraffin_Real*(1-br)
    aromatics = tank_obj_s_qr.Aromatics_Real*br + tank_obj_b_br.Aromatics_Real*(1-br)
    density = tank_obj_s_qr.Density_Real*br + tank_obj_b_br.Density_Real*(1-br)
    inipratio = tank_obj_s_qr.IN_IP_Ratio_Real*br + tank_obj_b_br.IN_IP_Ratio_Real*(1-br)

    olefins = tank_obj_s_qa.Olefins*br + tank_obj_b_ba.Olefins*(1-br)
    naphthene = tank_obj_s_qa.Naphthene*br + tank_obj_b_ba.Naphthene*(1-br)
    ibp = tank_obj_s_qa.IBP*br + tank_obj_b_ba.IBP*(1-br)
    fbp = tank_obj_s_qa.FBP*br + tank_obj_b_ba.FBP*(1-br)

    Input_Parameter_UserDefined.objects.filter(pk=instance.id).update(Paraffin_UD = paraffin, 
                                               Olefins_UD = olefins,Aromatics_UD = aromatics, 
                                               Naphthene_UD = naphthene,
                                               Density_UD = density, IBP_UD = ibp, FBP_UD = fbp, 
                                               tanks_Overall_Status = parent_obj)  


#Input Perameter for the User Defined Class
@receiver(post_save, sender = Input_Parameter_UserDefined)
def save_user_defined_output(sender, instance, **kwargs):

    if instance.Confirmation == False:

        parent_obj = Input_Parameter_UserDefined.objects.all().order_by('-id')[0]
    
        output = User_Defined_Model.user_defined_model_output(parent_obj)

        Output_Parameter_UserDefined.objects.create(Ethylene_UD= output[0], Propylene_UD = output[1], RPG_UD = output[2],
                                                    Benzene_UD = output[3],C4_Mix_UD = output[4], Fuel_Gas_UD = output[5], BD_UD = output[6],
                                                    input_Parameter_UserDefined = instance) 


#signals for the update next hour selection
@receiver(post_save, sender = Input_Parameter_UserDefined)
def update_next_hr_selection(sender, instance, **kwargs):

    if instance.Confirmation == True:

        parent_obj = Next_Hour_Selection.objects.all().order_by('-id')[0]

        Next_Hour_Selection.objects.filter(pk=parent_obj.id).update(U_D = True, R_N = False,
                                                                    B_F = False, P_M = False)


#signalsfor the Input_Parameter_Running
@receiver(post_save, sender = Next_Hour_Selection)
def save_input_parameter_running(sender, instance, **kwargs):
    if not (Input_Parameter_Running.objects.filter(tanks_Overall_Status = instance.tanks_Overall_Status).exists()):

        parent_obj = instance.tanks_Overall_Status
        previoushr = Next_Hour_Selection.objects.all().order_by('-id')[1]
    
        if previoushr.B_F == True:

            bf = Input_Parameter_BestFit.objects.all().order_by('-id')[1]
            totalload = bf.Naphtha_Load_BF + bf.LPG_Load_BF + bf.C5_Load_BF + bf.C6_Load_BF
            Input_Parameter_Running.objects.create(IN_IP_Ratio_RN = bf.IN_IP_Ratio_BF,
                                                Naphtha_Load_RN = bf.Naphtha_Load_BF, LPG_Load_RN = bf.LPG_Load_BF, 
                                                C5_Load_RN = bf.C5_Load_BF, C6_Load_RN = bf.C6_Load_BF,
                                                Naphtha_Heater_RN = bf.Naphtha_Heater_BF, COT_RN = bf.COT_BF, 
                                                GF_PDI_RN = bf.GF_PDI_BF, Suc_Pressure_RN = bf.Suc_Pressure_BF, 
                                                Total_Load_RN = totalload, Paraffin_RN = bf.Paraffin_BF, Olefins_RN = bf.Olefins_BF, 
                                                Aromatics_RN = bf.Aromatics_BF, Naphthene_RN = bf.Naphthene_BF,
                                                Density_RN = bf.Density_BF,IBP_RN = bf.IBP_BF,FBP_RN = bf.FBP_BF, 
                                                tanks_Overall_Status = parent_obj)
        
        if previoushr.P_M == True:

            pm = Input_Parameter_ProfitMax.objects.all().order_by('-id')[1]
            totalload = pm.Naphtha_Load_PM + pm.LPG_Load_PM + pm.C5_Load_PM + pm.C6_Load_PM
            Input_Parameter_Running.objects.create(IN_IP_Ratio_RN = pm.IN_IP_Ratio_PM,
                                                Naphtha_Load_RN = pm.Naphtha_Load_PM, LPG_Load_RN = pm.LPG_Load_PM, 
                                                C5_Load_RN = pm.C5_Load_PM, C6_Load_RN = pm.C6_Load_PM,
                                                Naphtha_Heater_RN = pm.Naphtha_Heater_PM, COT_RN = pm.COT_PM, 
                                                GF_PDI_RN = pm.GF_PDI_PM, Suc_Pressure_RN = pm.Suc_Pressure_PM,
                                                Total_Load_RN = totalload, Paraffin_RN = pm.Paraffin_PM, Olefins_RN = pm.Olefins_PM, 
                                                Aromatics_RN = pm.Aromatics_PM, Naphthene_RN = pm.Naphthene_PM,
                                                Density_RN = pm.Density_PM, IBP_RN = pm.IBP_PM, FBP_RN = pm.FBP_PM, 
                                                tanks_Overall_Status = parent_obj)

            
        if previoushr.U_D == True:

            tankoverall = Tanks_Overall_Status.objects.all().order_by('-id')[1]
            ud = Input_Parameter_UserDefined.objects.filter(Confirmation = True, tanks_Overall_Status = tankoverall).get()
            totalload = ud.Naphtha_Load_UD + ud.LPG_Load_UD + ud.C5_Load_UD + ud.C6_Load_UD
            Input_Parameter_Running.objects.create(IN_IP_Ratio_RN = ud.IN_IP_Ratio_UD,
                                                   Naphtha_Load_RN = ud.Naphtha_Load_UD, LPG_Load_RN = ud.LPG_Load_UD, 
                                                   C5_Load_RN = ud.C5_Load_UD, C6_Load_RN = ud.C6_Load_UD,
                                                   Naphtha_Heater_RN = ud.Naphtha_Heater_UD, COT_RN = ud.COT_UD, 
                                                   GF_PDI_RN = ud.GF_PDI_UD, Suc_Pressure_RN = ud.Suc_Pressure_UD,
                                                   Total_Load_RN = totalload, Paraffin_RN = ud.Paraffin_UD, Olefins_RN = ud.Olefins_UD, 
                                                   Aromatics_RN = ud.Aromatics_UD, Naphthene_RN = ud.Naphthene_UD,
                                                   Density_RN = ud.Density_UD, IBP_RN = ud.IBP_UD, FBP_RN = ud.FBP_UD, 
                                                   tanks_Overall_Status = parent_obj)

        if previoushr.R_N == True:
        
            rn = Input_Parameter_Running.objects.all().order_by('-id')[0]
            totalload = rn.Naphtha_Load_RN + rn.LPG_Load_RN + rn.C5_Load_RN + rn.C6_Load_RN
            parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
            #   oldoverallstatus = Tanks_Overall_Status.objects.all().order_by('-id')[1]

            suctiontank = parent_obj.Suction_Tank_No_RN
            blendingtank = parent_obj.Blending_Tank_No_RN
            br = parent_obj.Blend_Ratio_RN

            tank_obj_s = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = suctiontank).get()
            tank_obj_b = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = blendingtank).get()

            tank_obj_s_qr = Quality_Real.objects.filter(tank = tank_obj_s).get()
            tank_obj_b_br = Quality_Real.objects.filter(tank = tank_obj_b).get()

            tank_obj_s_qa = Quality_Avg.objects.filter(tank = tank_obj_s).get()
            tank_obj_b_ba = Quality_Avg.objects.filter(tank = tank_obj_b).get()

            paraffin = tank_obj_s_qr.Paraffin_Real*br + tank_obj_b_br.Paraffin_Real*(1-br)
            aromatics = tank_obj_s_qr.Aromatics_Real*br + tank_obj_b_br.Aromatics_Real*(1-br)
            density = tank_obj_s_qr.Density_Real*br + tank_obj_b_br.Density_Real*(1-br)
            inipratio = tank_obj_s_qr.IN_IP_Ratio_Real*br + tank_obj_b_br.IN_IP_Ratio_Real*(1-br)

            olefins = tank_obj_s_qa.Olefins*br + tank_obj_b_ba.Olefins*(1-br)
            naphthene = tank_obj_s_qa.Naphthene*br + tank_obj_b_ba.Naphthene*(1-br)
            ibp = tank_obj_s_qa.IBP*br + tank_obj_b_ba.IBP*(1-br)
            fbp = tank_obj_s_qa.FBP*br + tank_obj_b_ba.FBP*(1-br)            

            Input_Parameter_Running.objects.create(IN_IP_Ratio_RN = inipratio,
                                                   Naphtha_Load_RN = rn.Naphtha_Load_RN, LPG_Load_RN = rn.LPG_Load_RN, 
                                                   C5_Load_RN = rn.C5_Load_RN, C6_Load_RN = rn.C6_Load_RN,
                                                   Naphtha_Heater_RN = rn.Naphtha_Heater_RN, COT_RN = rn.COT_RN, 
                                                   GF_PDI_RN = rn.GF_PDI_RN, Suc_Pressure_RN = rn.Suc_Pressure_RN,
                                                   Total_Load_RN = totalload, Paraffin_RN = paraffin, Olefins_RN = aromatics, 
                                                   Aromatics_RN = aromatics, Naphthene_RN = naphthene,
                                                   Density_RN = density, IBP_RN = ibp, FBP_RN = fbp, 
                                                   tanks_Overall_Status = parent_obj)


#signals for the output parameter running
@receiver(post_save, sender = Input_Parameter_Running)
def save_output_parameter_running(sender, instance, **kwargs):

    output = [0] * 7
    output = random.sample(range(10, 100), 7)

    Output_Parameter_Running.objects.create(Ethylene_RN = output[0], Propylene_RN = output[1], RPG_RN = output[2],
                                            Benzene_RN = output[3], C4_Mix_RN = output[4], Fuel_Gas_RN = output[5], BD_RN = output[6],
                                            input_Parameter_Running = instance)      




#Output Perameters for the Running model 
@receiver(post_save, sender = Next_Hour_Selection)
def save_model_output_parameter_running(sender, instance, **kwargs):

    old_obj = Next_Hour_Selection.objects.all().order_by('-id')[1]
    if not (Model_Output_Parameter_Running.objects.filter(next_Hour_Selection = instance).exists() or Model_Output_Parameter_Running.objects.filter(next_Hour_Selection = old_obj).exists()):

        if old_obj.R_N == True:

            output = Running_Model_Output.running_model_output(instance)

            Model_Output_Parameter_Running.objects.create(Ethylene_RN_MO = output[0], Propylene_RN_MO = output[1], RPG_RN_MO = output[2],
                                                          Benzene_RN_MO = output[3], C4_Mix_RN_MO = output[4], Fuel_Gas_RN_MO = output[5], BD_RN_MO = output[6],
                                                          next_Hour_Selection = old_obj)  


#Output Perameters for the output comparasion class
@receiver(post_save, sender = Output_Parameter_Running)
def save_output_comparasion(sender, instance, **kwargs):

    parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[3]
    parent_obj_next = Tanks_Overall_Status.objects.all().order_by('-id')[2]
    nexthr_old_obj = Next_Hour_Selection.objects.filter().get(tanks_Overall_Status = parent_obj)

    if nexthr_old_obj.B_F == True:
    
        plantconstraints = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()
        inputbf = Input_Parameter_BestFit.objects.filter(plant_Constraints = plantconstraints).get()

        inputparameter = Input_Parameter_Running.objects.all().order_by('-id')[2]
        modeloutput = Output_Parameter_BestFit.objects.filter(input_Parameter_BestFit = inputbf).get()
        actualoutput = instance

        output = [0] * 7

        output[0] = modeloutput.Ethylene_BF
        output[1] = modeloutput.Propylene_BF
        output[2] = modeloutput.RPG_BF
        output[3] = modeloutput.C4_Mix_BF
        output[4] = modeloutput.Fuel_Gas_BF
        output[5] = modeloutput.Benzene_BF
        output[6] = modeloutput.BD_BF
    
    if nexthr_old_obj.P_M == True:

        inputpm = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()

        inputparameter = Input_Parameter_Running.objects.all().order_by('-id')[2]
        modeloutput = Output_Parameter_ProfitMax.objects.filter(input_Parameter_ProfitMax = inputpm).get()
        actualoutput = instance

        output = [0] * 7

        output[0] = modeloutput.Ethylene_PM
        output[1] = modeloutput.Propylene_PM
        output[2] = modeloutput.RPG_PM
        output[3] = modeloutput.C4_Mix_PM
        output[4] = modeloutput.Fuel_Gas_PM
        output[5] = modeloutput.Benzene_PM
        output[6] = modeloutput.BD_PM

    if nexthr_old_obj.U_D == True:
    
        inputud = Input_Parameter_UserDefined.objects.filter(tanks_Overall_Status = parent_obj, Confirmation = True).get()

        inputparameter = Input_Parameter_Running.objects.all().order_by('-id')[2]
        modeloutput = Output_Parameter_UserDefined.objects.filter(input_Parameter_UserDefined = inputud).get()
        actualoutput = instance

        output = [0] * 7

        output[0] = modeloutput.Ethylene_UD
        output[1] = modeloutput.Propylene_UD
        output[2] = modeloutput.RPG_UD
        output[3] = modeloutput.C4_Mix_UD
        output[4] = modeloutput.Fuel_Gas_UD
        output[5] = modeloutput.Benzene_UD
        output[6] = modeloutput.BD_UD

    if nexthr_old_obj.R_N == True:
        
        inputrn = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj).get()

        inputparameter = Input_Parameter_Running.objects.all().order_by('-id')[2]
       
        modeloutput = Model_Output_Parameter_Running.objects.filter(next_Hour_Selection = nexthr_old_obj).get()
        actualoutput = instance

        output = [0] * 7

        output[0] = modeloutput.Ethylene_RN_MO
        output[1] = modeloutput.Propylene_RN_MO
        output[2] = modeloutput.RPG_RN_MO
        output[3] = modeloutput.C4_Mix_RN_MO
        output[4] = modeloutput.Fuel_Gas_RN_MO
        output[5] = modeloutput.Benzene_RN_MO
        output[6] = modeloutput.BD_RN_MO

    Output_Comparision.objects.create(Total_Load = inputparameter.Total_Load_RN, Naphtha_Load = inputparameter.Naphtha_Load_RN , 
                                      LPG_Load = inputparameter.LPG_Load_RN, C5_Load = inputparameter.C5_Load_RN, C6_Load = inputparameter.C6_Load_RN,
                                      Naphtha_Heater = inputparameter.Naphtha_Heater_RN , COT = inputparameter.COT_RN,
                                      GF_PDI = inputparameter.GF_PDI_RN, Suc_Pressure = inputparameter.Suc_Pressure_RN, Paraffin = inputparameter.Paraffin_RN, 
                                      Olefins = inputparameter.Olefins_RN, Aromatics = inputparameter.Aromatics_RN, 
                                      Naphthene = inputparameter.Naphthene_RN, Density = inputparameter.Density_RN, 
                                      IBP = inputparameter.IBP_RN, FBP = inputparameter.FBP_RN, IN_IP_Ratio = inputparameter.IN_IP_Ratio_RN,
                                      Suction_Tank_No = parent_obj_next.Suction_Tank_No_RN, Blending_Tank_No = parent_obj_next.Blending_Tank_No_RN, 
                                      Blend_Ratio = parent_obj_next.Blend_Ratio_RN, Ethylene_Actual = actualoutput.Ethylene_RN,
                                      Propylene_Actual = actualoutput.Propylene_RN, RPG_Actual = actualoutput.RPG_RN,
                                      C4_Mix_Actual = actualoutput.C4_Mix_RN, Fuel_Gas_Actual = actualoutput.Fuel_Gas_RN, 
                                      Benzene_Actual = actualoutput.Benzene_RN, BD_Actual = actualoutput.BD_RN,
                                      Ethylene_Predicted = output[0], Propylene_Predicted = output[1] , RPG_Predicted =  output[2],
                                      C4_Mix_Predicted = output[3],  Fuel_Gas_Predicted = output[4],  Benzene_Predicted = output[5],
                                      BD_Predicted = output[6], output_Parameter_Running = instance )


#Output Perameters for the output comparasion class
@receiver(post_save, sender = Naphtha_Plan_Single_Month)
def save_naphtha_plan(sender, instance, **kwargs):



    date = instance.Date 
    date = date.strftime("%Y-%m-%d")
    month = datetime.datetime.strptime(date, "%Y-%m-%d").month
    year = datetime.datetime.strptime(date, "%Y-%m-%d").year



    array = Naphtha_Plan_All_Months.objects.all()

    flag = True
    for i in range(0,len(array)):
        M = datetime.datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").month
        Y = datetime.datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").year
        if M == month and Y == year:
            flag = False

    if flag:

        Naphtha_Plan_All_Months.objects.create( Month_Year = date)

    array = Naphtha_Plan_All_Months.objects.all()
    for i in range(0,len(array)):
        M = datetime.datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").month
        Y = datetime.datetime.strptime(array[i].Month_Year.strftime("%Y-%m-%d"), "%Y-%m-%d").year
        if M == month and Y == year: 

            Naphtha_Plan_Single_Month.objects.filter(pk=instance.id).update(Actual_NCU_TPD = 24*instance.Actual_NCU_TPH, 
                                                Budget_NCU_TPD = 24*instance.Budget_NCU_TPH,
                                                naphtha_Plan_All_Months = array[i])        

##Summary

    instance = Naphtha_Plan_Single_Month.objects.all().order_by('-id')[0]

    if (Naphtha_Plan_Summary.objects.filter(naphtha_Plan_All_Months = instance.naphtha_Plan_All_Months).exists()):

        
        obj = Naphtha_Plan_Summary.objects.filter(naphtha_Plan_All_Months = instance.naphtha_Plan_All_Months).get()
        consumptionncu = obj.Consumption_NCU + instance.Actual_NCU_TPD
        consumptioncpp = obj.Consumption_CPP + instance.Actual_CPP_TPD
        consumptiontotal = consumptionncu + consumptioncpp
        procurement_ADNOC = 0; procurement_IOC = 0; procurement_BPCL = 0; procurement_HPCL = 0; procurement_KPC = 0; procurement_SPOT = 0
        if instance.Source == "ADNOC":
            procurement_ADNOC = obj.Procurement_ADNOC + instance.Quantity
        if instance.Source == "IOC":
            procurement_IOC = obj.Procurement_IOC + instance.Quantity
        if instance.Source == "BPCL":
            procurement_BPCL = obj.Procurement_BPCL + instance.Quantity
        if instance.Source == "HPCL":
            procurement_HPCL = obj.Procurement_HPCL + instance.Quantity
        if instance.Source == "KPC":
            procurement_KPC = obj.Procurement_KPC + instance.Quantity
        if instance.Source == "SPOT":
            procurement_SPOT = obj.Procurement_SPOT + instance.Quantity
        procurementtotal = procurement_ADNOC + procurement_IOC + procurement_BPCL + procurement_HPCL + procurement_KPC +procurement_SPOT
            #
            
        arraythismonth = Naphtha_Plan_Single_Month.objects.filter(naphtha_Plan_All_Months = instance.naphtha_Plan_All_Months)
        days = len(arraythismonth)
        stock = [0] * days
        for i in range(0,days):
            stock[i] = arraythismonth[i].Total_Stock  

        mini = min(stock)
        maxa = max(stock)
            #
        avgstock = obj.Avg_Stock + instance.Total_Stock/days
        Max_Stock = maxa
        Min_Stock = mini

        opening_stock = arraythismonth[0].Total_Stock
        closing_stock = arraythismonth[days-1].Total_Stock
            
        Naphtha_Plan_Summary.objects.filter(pk=obj.id).update(Consumption_Total = consumptiontotal, 
                                            Consumption_NCU  = consumptionncu, Consumption_CPP = consumptioncpp, 
                                            Procurement_Total = procurementtotal, Procurement_ADNOC = procurement_ADNOC,
                                            Procurement_IOC = procurement_IOC,  Procurement_BPCL = procurement_BPCL,
                                            Procurement_HPCL = procurement_HPCL, Procurement_KPC = procurement_KPC,  
                                            Procurement_SPOT = procurement_SPOT, Opening_Stock = opening_stock,
                                            Closing_Stock = closing_stock, Avg_Stock = avgstock,  Min_Stock = Min_Stock,  
                                            Max_Stock = Max_Stock) 

    else:

        consumptiontotal = instance.Actual_NCU_TPD +  instance.Actual_CPP_TPD
        procurement_ADNOC = 0; procurement_IOC = 0; procurement_BPCL = 0; procurement_HPCL = 0; procurement_KPC = 0; procurement_SPOT = 0
        if instance.Source == "ADNOC":
            procurement_ADNOC = instance.Quantity
        if instance.Source == "IOC":
            procurement_IOC = instance.Quantity
        if instance.Source == "BPCL":
            procurement_BPCL = instance.Quantity
        if instance.Source == "HPCL":
            procurement_HPCL = instance.Quantity
        if instance.Source == "KPC":
            procurement_KPC = instance.Quantity
        if instance.Source == "SPOT":
            procurement_SPOT = instance.Quantity

        procurementtotal = procurement_ADNOC + procurement_IOC + procurement_BPCL + procurement_HPCL + procurement_KPC +procurement_SPOT
        
        
        Naphtha_Plan_Summary.objects.create(Consumption_Total = consumptiontotal, Consumption_NCU  = instance.Actual_NCU_TPD, Consumption_CPP = instance.Actual_CPP_TPD, 
                                            Procurement_Total = procurementtotal, Procurement_ADNOC = procurement_ADNOC,
                                            Procurement_IOC = procurement_IOC,  Procurement_BPCL = procurement_BPCL,
                                            Procurement_HPCL = procurement_HPCL, Procurement_KPC = procurement_KPC,  
                                            Procurement_SPOT = procurement_SPOT, Opening_Stock = instance.Total_Stock,
                                            Closing_Stock = instance.Total_Stock, Avg_Stock = instance.Total_Stock,
                                            Min_Stock = instance.Total_Stock, Max_Stock = instance.Total_Stock, 
                                            naphtha_Plan_All_Months = instance.naphtha_Plan_All_Months) 

     