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
    #one to many relation with the Tank_Over_All Status Class
    tanks_Overall_Status = models.ForeignKey(Tanks_Overall_Status,on_delete =models.CASCADE)

#Quality_Avg Class
class Quality_Avg(models.Model):
    Paraffin = models.FloatField()
    Olefins= models.FloatField()
    Aromatics = models.FloatField()
    Naphthene = models.FloatField()
    IN_IP_Ratio= models.FloatField()
    Density= models.FloatField()
    IBP= models.FloatField(null=True,blank=True)
    FBP = models.FloatField(null=True,blank=True)
    Sulfur= models.FloatField(null=True,blank=True)
    Colour= models.FloatField()
    RVP= models.FloatField(null=True,blank=True)
    #one to one relation with the Tank Class
    tank = models.OneToOneField(Tank , on_delete = models.CASCADE)

#Quality_Real Class
class Quality_Real(models.Model):
    Paraffin_Real= models.FloatField()
    Aromatics_Real= models.FloatField()
    Density_Real= models.FloatField()
    IN_IP_Ratio_Real= models.FloatField()
    #one to one relation with the Tank Class
    tank= models.OneToOneField(Tank,on_delete =models.CASCADE)

#Quality_NIR_Actual Class
class Quality_NIR_Actual(models.Model):
    Paraffin_NIR= models.FloatField()
    Aromatics_NIR=models.FloatField()
    Density_NIR= models.FloatField()
    IN_IP_Ratio_NIR= models.FloatField()
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    

#Quality_NIR_Pred Class
class Quality_NIR_Pred(models.Model):
    Paraffin_NIR_Pred= models.FloatField()
    Aromatics_NIR_Pred= models.FloatField()
    Density_NIR_Pred= models.FloatField()
    IN_IP_Ratio_NIR_Pred= models.FloatField()
    #one to one relation with the Tank_Over_All Status Class
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
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status= models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)

#Input_Parameter_Running Class
class Input_Parameter_Running(models.Model):
    Naphtha_Load_RN= models.FloatField()
    LPG_Load_RN= models.FloatField()
    C5_Load_RN= models.FloatField()
    C6_Load_RN= models.FloatField()
    Naphtha_Heater_RN= models.FloatField()
    COT_RN= models.FloatField()
    GF_PDI_RN= models.FloatField()
    Suc_Pressure_RN= models.FloatField()
    #Calculated_Field
    Total_Load_RN= models.FloatField(null=True,blank=True)
    Paraffin_RN= models.FloatField(null=True,blank=True)
    Olefins_RN= models.FloatField(null=True,blank=True)
    Aromatics_RN= models.FloatField(null=True,blank=True)
    Naphthene_RN= models.FloatField(null=True,blank=True)
    IN_IP_Ratio_RN= models.FloatField(null=True,blank=True)
    Density_RN= models.FloatField(null=True,blank=True)
    IBP_RN= models.FloatField(null=True,blank=True)
    FBP_RN= models.FloatField(null=True,blank=True)
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status= models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    #Load_Sum():, Blending_Avg():

 #Input_Parameter_BestFit Class
class Input_Parameter_BestFit(models.Model):
    Suction_Tank_No_BF = models.IntegerField()
    Blending_Tank_No_BF= models.IntegerField()
    Blend_Ratio_BF = models.FloatField()
    Naphtha_Load_BF = models.FloatField()
    LPG_Load_BF = models.FloatField()
    C5_Load_BF = models.FloatField()
    C6_Load_BF = models.FloatField()
    Naphtha_Heater_BF = models.IntegerField()
    COT_BF = models.FloatField()
    GF_PDI_BF = models.FloatField()
    Suc_Pressure_BF = models.FloatField()
    Paraffin_BF = models.FloatField()
    Olefins_BF = models.FloatField()
    Aromatics_BF = models.FloatField()
    Naphthene_BF = models.FloatField()
    IN_IP_Ratio_BF = models.FloatField()
    Density_BF = models.FloatField()
    IBP_BF= models.FloatField(null=True,blank=True)
    FBP_BF= models.FloatField(null=True,blank=True)
    #one to one relation with the Plant_Constraints Class
    plant_Constraints = models.OneToOneField(Plant_Constraints,on_delete = models.CASCADE)
    #Yield_Opt_Model(): + Plant Constraints

#Input_Parameter_ProfitMax Class
class Input_Parameter_ProfitMax(models.Model):
    Suction_Tank_No_PM = models.IntegerField()
    Blending_Tank_No_PM = models.IntegerField()
    Blend_Ratio_PM = models.FloatField()
    Naphtha_Load_PM = models.FloatField()
    LPG_Load_PM = models.FloatField()
    C5_Load_PM = models.FloatField()
    C6_Load_PM = models.FloatField()
    Naphtha_Heater_PM = models.IntegerField()
    COT_PM = models.FloatField()
    GF_PDI_PM = models.FloatField()
    Suc_Pressure_PM = models.FloatField()
    Paraffin_PM = models.FloatField()
    Olefins_PM = models.FloatField() 
    Aromatics_PM = models.FloatField()
    Naphthene_PM = models.FloatField()
    IN_IP_Ratio_PM = models.FloatField()
    Density_PM = models.FloatField()
    IBP_PM= models.FloatField(null=True,blank=True)
    FBP_PM= models.FloatField(null=True,blank=True)
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status= models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    #Yield_Opt_Model(): + LP_ProfitMax

#Input_Parameter_UserDefined Class
class Input_Parameter_UserDefined(models.Model):
    Suction_Tank_No_UD = models.IntegerField()
    Blending_Tank_No_UD = models.IntegerField()
    Blend_Ratio_UD = models.FloatField()
    Naphtha_Load_UD = models.FloatField()
    LPG_Load_UD = models.FloatField()
    C5_Load_UD = models.FloatField()
    C6_Load_UD = models.FloatField()
    Naphtha_Heater_UD = models.IntegerField()
    COT_UD = models.FloatField()
    GF_PDI_UD = models.FloatField()
    Suc_Pressure_UD = models.FloatField()

    #Claculated Fields
    Paraffin_UD = models.FloatField()
    Olefins_UD = models.FloatField()
    Aromatics_UD = models.FloatField()
    Naphthene_UD = models.FloatField()
    IN_IP_Ratio_UD = models.FloatField()
    Density_UD = models.FloatField()
    IBP_UD = models.FloatField(null=True,blank=True)
    FBP_UD = models.FloatField(null=True,blank=True)
    #one to one relation with the Quality_Real Class
    quality_Real = models.OneToOneField(Quality_Real,on_delete = models.CASCADE)
    #Blending_Avg():

#Output_Parameter_Running Class
class Output_Parameter_Running(models.Model):
    Ethylene_RN =  models.FloatField()
    Propylene_RN = models.FloatField()
    RPG_RN = models.FloatField()
    C4_Mix_RN = models.FloatField()
    Fuel_Gas_RN = models.FloatField()
    Benzene_RN = models.FloatField()
    BD_RN = models.FloatField()
    #one to one relation with the Quality_Real Class
    input_Parameter_Running = models.OneToOneField(Input_Parameter_Running,on_delete = models.CASCADE)

#Output_Parameter_BestFit
class Output_Parameter_BestFit(models.Model):
    Ethylene_BF = models.FloatField()
    Propylene_BF = models.FloatField()
    RPG_BF = models.FloatField()
    C4_Mix_BF = models.FloatField()
    Fuel_Gas_BF = models.FloatField()
    Benzene_BF = models.FloatField()
    BD_BF = models.FloatField()
    #one to one relation with the input_Parameter_BestFit Class
    input_Parameter_BestFit = models.OneToOneField(Input_Parameter_BestFit,on_delete = models.CASCADE)

#Output_Parameter_ProfitMax Class
class Output_Parameter_ProfitMax(models.Model):
    Ethylene_PM = models.FloatField()
    Propylene_PM = models.FloatField()
    RPG_PM = models.FloatField()
    C4_Mix_PM = models.FloatField()
    Fuel_Gas_PM = models.FloatField()
    Benzene_PM = models.FloatField()
    BD_PM = models.FloatField()
    #one to one relation with the input_Parameter_ProfitMax Class
    input_Parameter_ProfitMax = models.OneToOneField(Input_Parameter_ProfitMax,on_delete = models.CASCADE)

#Output_Parameter_UserDefined
class Output_Parameter_UserDefined(models.Model):
    Ethylene_UD = models.FloatField()
    Propylene_UD = models.FloatField()
    RPG_UD = models.FloatField()
    C4_Mix_UD = models.FloatField()
    Fuel_Gas_UD = models.FloatField()
    Benzene_UD = models.FloatField()
    BD_UD = models.FloatField()
    #one to one relation with the input_Parameter_UserDefined Class
    input_Parameter_UserDefined = models.OneToOneField(Input_Parameter_UserDefined,on_delete = models.CASCADE)

#New_Naphtha_Summary Class
class New_Naphtha_Summary(models.Model):
    Opening_Stock = models.IntegerField()
    Source = models.CharField(max_length = 50)
    PCN_NCU = models.IntegerField()
    PCN_CPP = models.IntegerField()
    FGN_CPP = models.IntegerField()
    CBFS_CPP = models.IntegerField()
    #Fields--from singlas
    Date = models.DateField()
    Vessel_Name = models.CharField(max_length=50)
    Supply_Quantity = models.IntegerField()
    #one to one relation with the tanks_Overall_Status Class
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)


#New_Naphtha Class
class New_Naphtha(models.Model):
    Transport_Type= models.CharField(max_length = 50)
    Ship_Name= models.CharField(max_length = 50)
    Supplier= models.CharField(max_length = 50)
    Date_Transfer_From = models.DateField()
    Date_Transfer_To = models.DateField()
    HOJ = models.IntegerField()
    Load_Port= models.CharField(max_length = 50)
    BL_Quantity = models.FloatField()
    Shore_Quantity = models.FloatField()
    #Calculated Fields
    Shortage_Quantity = models.FloatField()
    Remaining_Stock_Calculate = models.FloatField()
    #one to one relation with the new_Naphtha_Summary Class
    new_Naphtha_Summary = models.OneToOneField(New_Naphtha_Summary,on_delete = models.CASCADE)
    #Shortage_Calculate():
    #Remaining_Stock_Calculate():
    #New_Avg_Quality():

#Receipt_Tank Class
class Receipt_Tank(models.Model):
    Tank_No_1  = models.FloatField(default=0)
    Tank_No_2  = models.FloatField(default=0)
    Tank_No_3  = models.FloatField(default=0)
    Tank_No_4  = models.FloatField(default=0)
    Tank_No_5  = models.FloatField(default=0)
    #one to one relation with the new_Naphtha Class
    new_Naphtha = models.OneToOneField(New_Naphtha,on_delete = models.CASCADE)

#New_Naphtha_Quality_Supplier
class New_Naphtha_Quality_Supplier(models.Model):
    Paraffin = models.FloatField(null=True,blank=True)
    Olefins = models.FloatField(null=True,blank=True)
    Aromatics = models.FloatField(null=True,blank=True)
    Naphthene = models.FloatField(null=True,blank=True)
    IN_IP_Ratio = models.FloatField(null=True,blank=True)
    Density = models.FloatField(null=True,blank=True)
    IBP = models.FloatField(null=True,blank=True)
    FBP = models.FloatField(null=True,blank=True)
    Sulfur = models.FloatField(null=True,blank=True)
    Colour = models.FloatField(null=True,blank=True)
    RVP = models.FloatField(null=True,blank=True)
    #one to one relation with the new_Naphtha Class
    new_Naphtha = models.OneToOneField(New_Naphtha,on_delete = models.CASCADE)


#New_Naphtha_Quality_Lab Class
class New_Naphtha_Quality_Lab(models.Model):
    Paraffin = models.FloatField() 
    Olefins = models.FloatField()
    Aromatics = models.FloatField()
    Naphthene = models.FloatField()
    IN_IP_Ratio = models.FloatField()
    Density = models.FloatField()
    IBP = models.FloatField(null=True,blank=True)
    FBP = models.FloatField(null=True,blank=True)
    Sulfur = models.FloatField(null=True,blank=True)
    Colour = models.FloatField()
    RVP = models.FloatField(null=True,blank=True)
    #one to one relation with the new_Naphtha Class
    new_Naphtha = models.OneToOneField(New_Naphtha,on_delete = models.CASCADE)

#Naphtha_Plan_All_Months
class Naphtha_Plan_All_Months(models.Model):
    Month_Year = models.DateField()

#Naphtha_Plan_Single_Month
class Naphtha_Plan_Single_Month(models.Model):
    Date = models.DateField()
    Total_Stock = models.IntegerField()
    Usable_Stock = models.IntegerField()
    Source= models.CharField(max_length = 50)
    Quantity = models.IntegerField()
    Actual_NCU_TPH = models.IntegerField()
    Budget_NCU_TPH = models.IntegerField()
    Actual_CPP_TPD = models.IntegerField()
    Budget_CPP_TPD = models.IntegerField()
    Draft_Level = models.IntegerField()
    #Foreignkey relation with the naphtha_Plan_All_Months
    naphtha_Plan_All_Months = models.ForeignKey(Naphtha_Plan_All_Months,on_delete =models.CASCADE)
    #Total_Consumption():
    #Total_Procurement():
    #Total_Stock():

#Naphtha_Plan_Summary
class Naphtha_Plan_Summary(models.Model):
    #Claculated by singals model
    Consumption_Total = models.FloatField(null=True,blank=True)
    Consumption_NCU = models.FloatField(null=True,blank=True)
    Consumption_CPP = models.FloatField(null=True,blank=True)
    Procurement_Total = models.FloatField(null=True,blank=True)
    Procurement_ADNOC = models.FloatField(null=True,blank=True)
    Procurement_IOC = models.FloatField(null=True,blank=True)
    Procurement_BPCL = models.FloatField(null=True,blank=True)
    Procurement_HPCL = models.FloatField(null=True,blank=True)
    Procurement_KPC = models.FloatField(null=True,blank=True)
    Procurement_SPOT = models.FloatField(null=True,blank=True)
    Total_Stock = models.FloatField(null=True,blank=True)
    Opening_Stock = models.FloatField(null=True,blank=True)
    Closing_Stock = models.FloatField(null=True,blank=True)
    Avg_Stock = models.FloatField(null=True,blank=True)
    Min_Stock = models.FloatField(null=True,blank=True)
    Max_Stock = models.FloatField(null=True,blank=True)
    naphtha_Plan_All_Months = models.OneToOneField(Naphtha_Plan_All_Months,on_delete = models.CASCADE)





#Login Class
class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField( max_length=50)
    objects = models.Manager()


    
    
