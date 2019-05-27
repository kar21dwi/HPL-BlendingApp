from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints

#create all signals

#Tanks_Overall_Status signals

@receiver(post_save, sender=Tanks_Overall_Status)
def save_tank(sender, instance, **kwargs):
    suctiontank = instance.Suction_Tank_No_RN
    blendingtank = instance.Blending_Tank_No_RN
    #print ("********************************************")
    #print (suctiontank)
    #print ("********************************************")
    old_obj = Tanks_Overall_Status.objects.all().order_by('-id')[1]
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

  

        Tank.objects.create(Level = new_level, Receiving_Naphtha = receiving, Tank_No =i+1,tanks_Overall_Status= instance)
     

        
    
#Tank Signal

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
                                Colour = colournew, RVP = rvpnew, tank = instance)
    else:
        Quality_Avg.objects.create(Paraffin = old_obj_qualityavg.Paraffin, Olefins = old_obj_qualityavg.Olefins, 
                                Aromatics = old_obj_qualityavg.Aromatics, Naphthene = old_obj_qualityavg.Naphthene, 
                                IN_IP_Ratio = old_obj_qualityavg.IN_IP_Ratio, Density = old_obj_qualityavg.Density,
                                IBP = old_obj_qualityavg.IBP, FBP = old_obj_qualityavg.IBP,Sulfur = old_obj_qualityavg.Sulfur, 
                                Colour = old_obj_qualityavg.Colour, RVP = old_obj_qualityavg.RVP, tank = instance)
 
 #Quality_Avg Signal
@receiver(post_save, sender=Quality_Avg)
def update_tank_weight(sender, instance, **kwargs):
    
    weight = instance.Density*( instance.tank.Level)*3.14*10.8*10.8*9.8
    Tank.objects.filter(pk=instance.tank.id).update(Weight = round(weight/1000 , 2))

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

    nirparaffin = old_obj_qualityavg_s.Paraffin*br + old_obj_qualityavg_b.Paraffin*(1-br)
    niraromatics = old_obj_qualityavg_s.Aromatics*br + old_obj_qualityavg_b.Aromatics*(1-br)
    nirdensity = old_obj_qualityavg_s.Density*br + old_obj_qualityavg_b.Density*(1-br)
    nirinipratio = old_obj_qualityavg_s.IN_IP_Ratio*br + old_obj_qualityavg_b.IN_IP_Ratio*(1-br)

    Quality_NIR_Actual.objects.create(Paraffin_NIR = nirparaffin, Aromatics_NIR = niraromatics, 
                                      IN_IP_Ratio_NIR = nirinipratio, Density_NIR = nirdensity, tanks_Overall_Status = instance)


@receiver(post_save, sender=Tanks_Overall_Status)
def save_plant_constraints(sender, instance, **kwargs):
    
   
    Plant_Constraints.objects.create(Max_Ethylene = 76, Max_Propylene = 40, Max_RPG = 60, Max_Benzene = 1.4,
                                     Max_C4_Mix = 22, Max_Fuel_Gas = 40, Max_BD = 1.9,tanks_Overall_Status = instance)

