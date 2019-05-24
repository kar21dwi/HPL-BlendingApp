
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#from djangoapp.api.models import Blending, Tanks_Overall, Average_Quality


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