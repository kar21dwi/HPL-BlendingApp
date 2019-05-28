from django.db import models

#from django.contrib.auth import get_user_model

#Define All classes 

#Tanks_Overall_Status Class
class Tanks_Overall_Status(models.Model):
    Date_Time =models.DateTimeField()
    Suction_Tank_No_RN= models.IntegerField(null=True,blank=True)
    Blending_Tank_No_RN= models.IntegerField(null=True,blank=True)
    Blend_Ratio_RN= models.FloatField(null=True,blank=True)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Tanks_Overall_Status"

#Next_Hour_Selection Class
class Next_Hour_Selection(models.Model):
    U_D = models.BooleanField()
    B_F = models.BooleanField()
    P_M = models.BooleanField()
    R_N = models.BooleanField()
    #one to many relation with the Tank_Over_All_Status Class
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete =models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Next_Hour_Selection"

#Model_Output_Parameter_Running
class Model_Output_Parameter_Running(models.Model):
    Ethylene_RN_MO = models.FloatField()
    Propylene_RN_MO = models.FloatField()
    RPG_RN_MO = models.FloatField()
    C4_Mix_RN_MO = models.FloatField()
    Fuel_Gas_RN_MO = models.FloatField()
    Benzene_RN_MO = models.FloatField()
    BD_RN_MO = models.FloatField()
    #one to many relation with the Next_Hour_Selection Class
    next_Hour_Selection = models.OneToOneField(Next_Hour_Selection,on_delete =models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Model_Output_Parameter_Running"

#Tank Class
class Tank(models.Model):
    Tank_No = models.IntegerField()
    Level = models.FloatField()
    Weight = models.FloatField(null=True,blank=True)
    Receiving_Naphtha = models.BooleanField()
    #one to many relation with the Tank_Over_All Status Class
    tanks_Overall_Status = models.ForeignKey(Tanks_Overall_Status,on_delete =models.CASCADE)
    #Calculated Field
    #Weight,
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Tank"

#Quality_Avg Class
class Quality_Avg(models.Model):
    Paraffin = models.FloatField()
    Olefins= models.FloatField()
    Aromatics = models.FloatField()
    Naphthene = models.FloatField()
    IN_IP_Ratio= models.FloatField()
    Density= models.FloatField()
    IBP= models.FloatField(default=0)
    FBP = models.FloatField(default=0)
    Sulfur= models.FloatField(default=0)
    Colour= models.FloatField()
    RVP= models.FloatField(default=0)
    #one to one relation with the Tank Class
    tank = models.OneToOneField(Tank , on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Quality_Avg"    

#Quality_Real Class
class Quality_Real(models.Model):
    Paraffin_Real= models.FloatField()
    Aromatics_Real= models.FloatField()
    Density_Real= models.FloatField()
    IN_IP_Ratio_Real= models.FloatField()
    #one to one relation with the Tank Class
    tank= models.OneToOneField(Tank,on_delete =models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Quality_Real"

#Quality_NIR_Actual Class
class Quality_NIR_Actual(models.Model):
    Paraffin_NIR= models.FloatField()
    Aromatics_NIR=models.FloatField()
    Density_NIR= models.FloatField()
    IN_IP_Ratio_NIR= models.FloatField()
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Quality_NIR_Actual"

#Quality_NIR_Pred Class
class Quality_NIR_Pred(models.Model):
    Paraffin_NIR_Pred= models.FloatField()
    Aromatics_NIR_Pred= models.FloatField()
    Density_NIR_Pred= models.FloatField()
    IN_IP_Ratio_NIR_Pred= models.FloatField()
    #one to one relation with the Tank_Over_All Status Class
    tanks_Overall_Status=  models.ForeignKey(Tanks_Overall_Status,on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Quality_NIR_Pred"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Plant_Constraints"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Input_Parameter_Running"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Input_Parameter_BestFit"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Input_Parameter_ProfitMax"

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
    Paraffin_UD = models.FloatField(null=True,blank=True)
    Olefins_UD = models.FloatField(null=True,blank=True)
    Aromatics_UD = models.FloatField(null=True,blank=True)
    Naphthene_UD = models.FloatField(null=True,blank=True)
    IN_IP_Ratio_UD = models.FloatField(null=True,blank=True)
    Density_UD = models.FloatField(null=True,blank=True)
    IBP_UD = models.FloatField(null=True,blank=True)
    FBP_UD = models.FloatField(null=True,blank=True)
    #one to one relation with the Quality_Real Class
    quality_Real = models.OneToOneField(Quality_Real,on_delete = models.CASCADE)
    #Blending_Avg():
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Input_Parameter_UserDefined"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Output_Parameter_Running"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Output_Parameter_BestFit"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Output_Parameter_ProfitMax"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Output_Parameter_UserDefined"

#Output_Comparision
class Output_Comparision(models.Model):
    Total_Load = models.FloatField()
    Naphtha_Load = models.FloatField()
    LPG_Load = models.FloatField()
    C5_Load = models.FloatField()
    C6_Load = models.FloatField()
    Naphtha_Heater = models.IntegerField()
    COT = models.FloatField()
    GF_PDI = models.FloatField()
    Suc_Pressure = models.FloatField()
    Paraffin = models.FloatField()
    Olefins = models.FloatField() 
    Aromatics = models.FloatField()
    Naphthene = models.FloatField()
    IN_IP_Ratio = models.FloatField()
    Density = models.FloatField()
    IBP = models.FloatField(null=True,blank=True)
    FBP = models.FloatField(null=True,blank=True)
    Suction_Tank_No = models.IntegerField()
    Blending_Tank_No = models.IntegerField()
    Blend_Ratio = models.FloatField()

    Ethylene_Actual = models.FloatField()
    Propylene_Actual = models.FloatField()
    RPG_Actual = models.FloatField()
    C4_Mix_Actual = models.FloatField()
    Fuel_Gas_Actual = models.FloatField()
    Benzene_Actual = models.FloatField()
    BD_Actual = models.FloatField()

    Ethylene_Predicted = models.FloatField()
    Propylene_Predicted = models.FloatField()
    RPG_Predicted = models.FloatField()
    C4_Mix_Predicted = models.FloatField()
    Fuel_Gas_Predicted = models.FloatField()
    Benzene_Predicted = models.FloatField()
    BD_Predicted = models.FloatField()
    output_Parameter_Running = models.OneToOneField(Output_Parameter_Running,on_delete =models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Output_Comparision"

#New_Naphtha Class
class New_Naphtha(models.Model):
    Transport_Type= models.CharField(max_length = 50)
    Date_Transfer_From = models.DateField()
    Date_Transfer_To = models.DateField()
    HOJ = models.IntegerField()
    Load_Port= models.CharField(max_length = 50)
    BL_Quantity = models.FloatField()
    Shore_Quantity = models.FloatField()
    Opening_Stock = models.IntegerField(null=True,blank=True)
    Source = models.CharField(max_length = 50)
    PCN_NCU = models.IntegerField(null=True,blank=True)
    PCN_CPP = models.IntegerField(null=True,blank=True)
    FGN_CPP = models.IntegerField(null=True,blank=True)
    CBFS_CPP = models.IntegerField(null=True,blank=True)
    Vessel_Name = models.CharField(max_length=50)
    #Calculated Fields 
    Shortage_Quantity = models.FloatField(null=True,blank=True) 
    #one to one relation with the tanks_Overall_Status Class
    tanks_Overall_Status = models.OneToOneField(Tanks_Overall_Status,on_delete = models.CASCADE)
    #Shortage_Calculate():
    #Remaining_Stock_Calculate():
    #New_Avg_Quality():
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "New_Naphtha"

#New_Naphtha_Quality_Lab Class
class New_Naphtha_Quality_Lab(models.Model):
    Paraffin = models.FloatField() 
    Olefins = models.FloatField()
    Aromatics = models.FloatField()
    Naphthene = models.FloatField()
    IN_IP_Ratio = models.FloatField()
    Density = models.FloatField()
    IBP = models.FloatField(default=0)
    FBP = models.FloatField(default=0)
    Sulfur = models.FloatField(default=0)
    Colour = models.FloatField()
    RVP = models.FloatField(default=0)
    #one to one relation with the new_Naphtha Class
    new_Naphtha = models.OneToOneField(New_Naphtha,on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "New_Naphtha_Quality_Lab"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "New_Naphtha_Quality_Supplier"

#Receipt_Tank Class
class Receipt_Tank(models.Model):
    Tank_No_1  = models.FloatField(default=0)
    Tank_No_1_Receiving = models.FloatField(default=-1)
    Tank_No_2  = models.FloatField(default=0)
    Tank_No_2_Receiving = models.FloatField(default=-1)    
    Tank_No_3  = models.FloatField(default=0)
    Tank_No_3_Receiving = models.FloatField(default=-1)    
    Tank_No_4  = models.FloatField(default=0)
    Tank_No_4_Receiving = models.FloatField(default=-1)   
    Tank_No_5  = models.FloatField(default=0)
    Tank_No_5_Receiving = models.FloatField(default=-1)   
    #one to one relation with the new_Naphtha Class
    new_Naphtha = models.OneToOneField(New_Naphtha,on_delete = models.CASCADE)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Receipt_Tank"

#Naphtha_Plan_All_Months
class Naphtha_Plan_All_Months(models.Model):
    Month_Year = models.DateField()
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Naphtha_Plan_All_Months"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Naphtha_Plan_Single_Month"

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
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Naphtha_Plan_Summary"
       
#Login Class
class Login(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField( max_length=50)
    objects = models.Manager()
    class Meta:
       verbose_name_plural = "Login"

    
    
