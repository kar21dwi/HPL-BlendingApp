from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints
from djangoapp.api.models import Quality_NIR_Pred, Next_Hour_Selection, Input_Parameter_BestFit
from djangoapp.api.models import Output_Parameter_BestFit, Input_Parameter_ProfitMax, Quality_Real,Output_Parameter_ProfitMax
from djangoapp.dlmodels.qualityreal import Quality_Real_Model
from djangoapp.dlmodels.bestfit import Best_Fit_Model
from djangoapp.dlmodels.profitmax import Profit_Max_Model
import numpy

#create all signals

#signals
@receiver(post_save, sender=Tanks_Overall_Status)
def update_tank_overall(sender, instance, **kwargs):

   old_obj_next_hr = Next_Hour_Selection.objects.all().order_by('-id')[0]
   parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[1]
   '''
   if old_obj_next_hr.U_D == True:
        #hjkhkjh
        '''
   if old_obj_next_hr.B_F == True:
       bestfit = Input_Parameter_BestFit.objects.filter(plant_Constraints = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()).get()

       Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = bestfit.Suction_Tank_No_BF,
                                             Blending_Tank_No_RN = bestfit.Blending_Tank_No_BF, 
                                             Blend_Ratio_RN = bestfit.Blend_Ratio_BF)  
                                            
   if old_obj_next_hr.P_M == True:
        profitmax = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()

        Tanks_Overall_Status.objects.filter(pk=instance.id).update(Suction_Tank_No_RN = profitmax.Suction_Tank_No_PM,
                                            Blending_Tank_No_RN = profitmax.Blending_Tank_No_PM, 
                                            SBlend_Ratio_RN = profitmax.Blend_Ratio_PM)       
'''
   else:
       old_obj_next_hr.R_N == True:
       
'''
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
def save_best_fit_output(sender, instance, **kwargs):

    output = Profit_Max_Model.profit_max_model_output(instance)

    Output_Parameter_ProfitMax.objects.create(Ethylene_PM = output[0], Propylene_PM = output[1], RPG_PM = output[2],
                                              Benzene_PM = output[3],C4_Mix_PM = output[4], Fuel_Gas_PM = output[5], BD_PM = output[6],
                                              input_Parameter_ProfitMax = instance)    
