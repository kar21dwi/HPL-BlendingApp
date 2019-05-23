from django.contrib import admin

from .models import Tanks_Overall_Status,Tank,Quality_Avg,Quality_Real,Quality_NIR_Actual,Quality_NIR_Pred,Plant_Constraints,Input_Parameter_Running,Input_Parameter_BestFit,Input_Parameter_ProfitMax,Input_Parameter_UserDefined,Output_Parameter_Running,Output_Parameter_BestFit,Output_Parameter_ProfitMax,Output_Parameter_UserDefined,New_Naphtha_Summary,New_Naphtha,Receipt_Tank,New_Naphtha_Quality_Supplier,New_Naphtha_Quality_Lab,Naphtha_Plan_All_Months,Naphtha_Plan_Single_Month,Naphtha_Plan_Summary,Login

# Register your models here.
admin.site.register(Tanks_Overall_Status)
admin.site.register(Tank)
admin.site.register(Quality_Avg)
admin.site.register(Quality_Real)
admin.site.register(Quality_NIR_Actual)
admin.site.register(Quality_NIR_Pred)
admin.site.register(Plant_Constraints)
admin.site.register(Input_Parameter_Running)
admin.site.register(Input_Parameter_BestFit)
admin.site.register(Input_Parameter_ProfitMax)
admin.site.register(Input_Parameter_UserDefined)
admin.site.register(Output_Parameter_Running)
admin.site.register(Output_Parameter_BestFit)
admin.site.register(Output_Parameter_ProfitMax)
admin.site.register(Output_Parameter_UserDefined)
admin.site.register(New_Naphtha_Summary)
admin.site.register(New_Naphtha)
admin.site.register(Receipt_Tank)
admin.site.register(New_Naphtha_Quality_Supplier)
admin.site.register(New_Naphtha_Quality_Lab)
admin.site.register(Naphtha_Plan_All_Months)
admin.site.register(Naphtha_Plan_Single_Month)
admin.site.register(Naphtha_Plan_Summary)
admin.site.register(Login)

