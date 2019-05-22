from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
#from django.contrib.auth import get_user_model

#Define All classes 

#Tanks_Overall_Status Class
class Tanks_Overall_Status(models.Model):
    Suction_Tank_No_RN= models.IntegerField()
    Blending_Tank_No_RN= models.IntegerField()
    Blend_Ratio_RN= models.FloatField()
    Date_Time =models.DateTimeField()

#Tank Class
class Tank(models.Model):
    Tank_No = models.IntegerField()
    Level = models.FloatField()
    Weight = models.FloatField()
    tanks_Overall_Status = models.ForeignKey(Tanks_Overall_Status,on_delete =models.CASCADE)

#Quality_Avg Class
class Quality_Avg(models.Model):
    Paraffin = models.FloatField(max_length=10)
    Olefins= models.FloatField(max_length=10)
    Aromatics = models.FloatField(max_length=10)
    Naphthene = models.FloatField()
    IN_IP_Ratio= models.FloatField()
    Density= models.FloatField()
    IBP= models.FloatField(null=True,blank=True)
    FBP = models.FloatField(null=True,blank=True,)
    Sulfur= models.FloatField(null=True,blank=True,)
    Colour= models.CharField(max_length = 50, null=True,blank=True,)
    RVP= models.FloatField(null=True,blank=True,)
    tank = models.OneToOneField(Tank , on_delete = models.CASCADE)

#Quality_Real Class
class Quality_Real(models.Model):
    Paraffin_Real= models.FloatField()
    Aromatics_Real= models.FloatField()
    Density_Real= models.FloatField()
    IN_IP_Ratio_Real= models.FloatField()
    tank= models.OneToOneField(Tank,on_delete =models.CASCADE)

#Quality_NIR_Actual Class
class Quality_NIR_Actual(models.Model):
    Paraffin_NIR= models.FloatField()
    Aromatics_NIR=models.FloatField()
    Density_NIR= models.FloatField()
    IN_IP_Ratio_NIR= models.FloatField()
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    

#Quality_NIR_Pred Class
class Quality_NIR_Pred(models.Model):
    Paraffin_NIR_Pred= models.FloatField()
    Aromatics_NIR_Pred= models.FloatField()
    Density_NIR_Pred= models.FloatField()
    IN_IP_Ratio_NIR_Pred= models.FloatField()
    tanks_Overall_Status=  models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)

#Plant_Constraints Class
class Plant_Constraints(models.Model):
    Max_Ethylene= models.FloatField()
    Max_Propylene= models.FloatField()
    Max_RPG= models.FloatField()
    Max_C4_Mix= models.FloatField()
    Max_Fuel_Gas= models.FloatField()
    Max_Benzene= models.FloatField()
    Max_BD= models.FloatField()
    tanks_Overall_Status= models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)

#Input_Parameter_Running Class
class Sample(models.Model):
    Naphtha_Load_RN = models.FloatField(max_length=10)
    LPG_Load_RN = models.FloatField(max_length=10)
    C5_Load_RN = models.FloatField(max_length=10)
    C6_Load_RN = models.FloatField(max_length=10)


class sum(models.Model):
    sample = models.OneToOneField(Sample , on_delete = models.CASCADE)
    

@receiver(post_save, sender=Sample)
def save_sum(sender, instance, **kwargs):
    print("hjgugytffytvuguguygihkjnkjohioj")
    instance.sum.save()


#Login Class
class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField( max_length=50)
    objects = models.Manager()


    
    
