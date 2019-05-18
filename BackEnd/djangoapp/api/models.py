from django.db import models


# Create your models here.
#Tank Details Model
class Tank(models.Model):
    Avg_Quality = models.CharField(max_length=32)
    Real_Time_Quality= models.CharField(max_length=256)
    NIR_Reading = models.IntegerField()
    objects = models.Manager()

#Login Model
class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField( max_length=50)
    objects = models.Manager()


    
    
