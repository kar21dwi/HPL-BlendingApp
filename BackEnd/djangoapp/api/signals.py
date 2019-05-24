
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg 


'''
@receiver(post_save, sender=Blending)
def create_total(sender, instance, created, **kwargs):
    if created:
        print("********************************")
        print(instance.LPG)
        print("********************************")
        total.objects.create(blending=instance)
'''

'''
@receiver(post_save, sender=Blending)
def save_total(sender, instance, **kwargs):
       suctiontank = instance.tanks_overall.suction_tank
       blendingtank = instance.tanks_overall.blending_tank
       br = instance.tanks_overall.blend_ratio
       
       p_suc = Average_Quality.objects.filter(tanks_overall=instance.tanks_overall , tank_no=suctiontank).get().paraffin
       p_blend = Average_Quality.objects.filter(tanks_overall=instance.tanks_overall , tank_no=blendingtank).get().paraffin
       o_suc = Average_Quality.objects.filter(tanks_overall_id=instance.tanks_overall , tank_no=suctiontank).get().olefin
       o_blend = Average_Quality.objects.filter(tanks_overall_id=instance.tanks_overall , tank_no=blendingtank).get().olefin
       a_suc = Average_Quality.objects.filter(tanks_overall_id=instance.tanks_overall , tank_no=suctiontank).get().aromatics
       a_blend = Average_Quality.objects.filter(tanks_overall_id=instance.tanks_overall , tank_no=blendingtank).get().aromatics
       
       
       tl = instance.Naphtha + instance.LPG
       pb = p_suc*br + p_blend*(1-br)
       ob = o_suc*br + o_blend*(1-br)
       ab = a_suc*br + a_blend*(1-br)

       Blending.objects.filter(pk=instance.id).update(total_load=tl)
       Blending.objects.filter(pk=instance.id).update(paraffin_blended=pb)
       Blending.objects.filter(pk=instance.id).update(olefin_blended=ob)
       Blending.objects.filter(pk=instance.id).update(aromatics_blended=ab)
   '''
@receiver(post_save, sender=Tanks_Overall_Status)
def save_total(sender, instance, **kwargs):
    suctiontank = instance.Suction_Tank_No_RN
    blendingtank = instance.Blending_Tank_No_RN
    print ("********************************************")
    print (suctiontank)
    print ("********************************************")

    old_obj = Tanks_Overall_Status.objects.filter(pk=(instance.id - 4)).get()
    old_tank = Tank.objects.filter(tanks_Overall_Status = old_obj , Tank_No=1).get()
    old_level = Tank.objects.filter(tanks_Overall_Status = old_obj , Tank_No=1).get().Level

    old_density_quaity_avg = Quality_Avg.objects.filter(tank= old_tank).get().Density


    if  suctiontank==1 or blendingtank==1:
        new_level = old_level - 100
    else:
        new_level = old_level

    
    new_weight = old_density_quaity_avg*new_level*3.14*8400*8400*10

    Tank.objects.create(Level = new_level, Weight = new_weight, Tank_No =1,tanks_Overall_Status= instance)