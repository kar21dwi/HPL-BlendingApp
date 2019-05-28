from django.contrib import admin

from .models import Tanks_Overall_Status,Tank,Quality_Avg,Quality_Real,Quality_NIR_Actual
from .models import Quality_NIR_Pred,Plant_Constraints,Input_Parameter_Running,Input_Parameter_BestFit
from .models import Input_Parameter_ProfitMax,Output_Parameter_Running,Output_Parameter_BestFit
from .models import Output_Parameter_ProfitMax, Input_Parameter_UserDefined, Output_Parameter_UserDefined
from .models import New_Naphtha,Receipt_Tank,New_Naphtha_Quality_Supplier,New_Naphtha_Quality_Lab
from .models import Naphtha_Plan_All_Months,Naphtha_Plan_Single_Month,Naphtha_Plan_Summary
from .models import Next_Hour_Selection,Model_Output_Parameter_Running,Output_Comparision
from .models import Login

from django.contrib.admin import site
from django.apps import apps
from django import template
from django.utils.text import capfirst
from django.contrib.auth.models import User


class Tanks_Overall_StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'Date_Time', 'Suction_Tank_No_RN', 'Blending_Tank_No_RN', 'Blend_Ratio_RN')
    list_editable = ('Date_Time', 'Suction_Tank_No_RN', 'Blending_Tank_No_RN', 'Blend_Ratio_RN')
    list_display_links = ('id',  )
    search_fields = ('Date_Time' , '')

class Next_Hour_SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'U_D', 'B_F', 'P_M', 'R_N', 'tanks_Overall_Status')
    list_editable = ('U_D', 'B_F', 'P_M', 'R_N', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('U_D' , '')

class Model_Output_Parameter_RunningAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ethylene_RN_MO', 'Propylene_RN_MO', 'RPG_RN_MO', 'C4_Mix_RN_MO',
     'Fuel_Gas_RN_MO', 'Benzene_RN_MO', 'BD_RN_MO', 'next_Hour_Selection')
    list_editable = ('Ethylene_RN_MO', 'Propylene_RN_MO', 'RPG_RN_MO', 'C4_Mix_RN_MO',
     'Fuel_Gas_RN_MO', 'Benzene_RN_MO', 'BD_RN_MO', 'next_Hour_Selection')
    list_display_links = ('id', )
    search_fields = ('Ethylene_RN_MO' , '')

class TankAdmin(admin.ModelAdmin):
    list_display = ('id', 'Tank_No', 'Level', 'Weight', 'Receiving_Naphtha', 'tanks_Overall_Status')
    list_editable = ('Tank_No', 'Level', 'Weight', 'Receiving_Naphtha', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Level' , '')

class Quality_AvgAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'tank')
    list_editable = ('Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'tank')
    list_display_links = ('id', )
    search_fields = ('Paraffin' , '')

class Quality_RealAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin_Real', 'Aromatics_Real', 'Density_Real', 'IN_IP_Ratio_Real', 'tank')
    list_editable = ('Paraffin_Real', 'Aromatics_Real', 'Density_Real', 'IN_IP_Ratio_Real', 'tank')
    list_display_links = ('id', )
    search_fields = ('Paraffin_Real' , '')

class Quality_NIR_ActualAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin_NIR', 'Aromatics_NIR', 'Density_NIR', 'IN_IP_Ratio_NIR', 'tanks_Overall_Status')
    list_editable = ('Paraffin_NIR', 'Aromatics_NIR', 'Density_NIR', 'IN_IP_Ratio_NIR', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Paraffin_NIR' , '')

class Quality_NIR_PredAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin_NIR_Pred', 'Aromatics_NIR_Pred', 'Density_NIR_Pred', 'IN_IP_Ratio_NIR_Pred',
    'tanks_Overall_Status')
    list_editable = ('Paraffin_NIR_Pred', 'Aromatics_NIR_Pred', 'Density_NIR_Pred', 'IN_IP_Ratio_NIR_Pred',
    'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Paraffin_NIR_Pred' , '')

class Plant_ConstraintsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Max_Ethylene', 'Max_Propylene', 'Max_RPG', 'Max_C4_Mix', 'Max_Fuel_Gas', 'Max_Benzene',
    'Max_BD', 'tanks_Overall_Status')
    list_editable = ('Max_Ethylene', 'Max_Propylene', 'Max_RPG', 'Max_C4_Mix', 'Max_Fuel_Gas', 'Max_Benzene',
    'Max_BD', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Max_Ethylene' , '')

class Input_Parameter_RunningAdmin(admin.ModelAdmin):
    list_display = ('id', 'Naphtha_Load_RN', 'LPG_Load_RN', 'C5_Load_RN', 'C6_Load_RN', 'Naphtha_Heater_RN', 'COT_RN',
    'GF_PDI_RN', 'Suc_Pressure_RN', 'Total_Load_RN', 'Paraffin_RN', 'Olefins_RN', 'Aromatics_RN', 'Naphthene_RN',
    'IN_IP_Ratio_RN', 'Density_RN', 'IBP_RN', 'FBP_RN', 'tanks_Overall_Status')
    list_editable = ('Naphtha_Load_RN', 'LPG_Load_RN', 'C5_Load_RN', 'C6_Load_RN', 'Naphtha_Heater_RN', 'COT_RN',
    'GF_PDI_RN', 'Suc_Pressure_RN', 'Total_Load_RN', 'Paraffin_RN', 'Olefins_RN', 'Aromatics_RN', 'Naphthene_RN',
    'IN_IP_Ratio_RN', 'Density_RN', 'IBP_RN', 'FBP_RN', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Naphtha_Load_RN' , '')

class Input_Parameter_BestFitAdmin(admin.ModelAdmin):
    list_display = ('id', 'Suction_Tank_No_BF', 'Blending_Tank_No_BF', 'Blend_Ratio_BF', 'Naphtha_Load_BF', 'LPG_Load_BF',
    'C5_Load_BF', 'C6_Load_BF', 'Naphtha_Heater_BF', 'COT_BF', 'GF_PDI_BF', 'Suc_Pressure_BF', 'Paraffin_BF', 'Olefins_BF',
    'Aromatics_BF', 'Naphthene_BF', 'IN_IP_Ratio_BF', 'Density_BF', 'IBP_BF', 'FBP_BF', 'plant_Constraints')
    list_editable = ('Suction_Tank_No_BF', 'Blending_Tank_No_BF', 'Blend_Ratio_BF', 'Naphtha_Load_BF', 'LPG_Load_BF',
    'C5_Load_BF', 'C6_Load_BF', 'Naphtha_Heater_BF', 'COT_BF', 'GF_PDI_BF', 'Suc_Pressure_BF', 'Paraffin_BF', 'Olefins_BF',
    'Aromatics_BF', 'Naphthene_BF', 'IN_IP_Ratio_BF', 'Density_BF', 'IBP_BF', 'FBP_BF', 'plant_Constraints')
    list_display_links = ('id', )
    search_fields = ('Suction_Tank_No_BF' , '')

class Input_Parameter_ProfitMaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'Suction_Tank_No_PM', 'Blending_Tank_No_PM', 'Blend_Ratio_PM', 'Naphtha_Load_PM', 'LPG_Load_PM',
    'C5_Load_PM', 'C6_Load_PM', 'Naphtha_Heater_PM', 'COT_PM', 'GF_PDI_PM', 'Suc_Pressure_PM', 'Paraffin_PM', 'Olefins_PM',
    'Aromatics_PM', 'Naphthene_PM', 'IN_IP_Ratio_PM', 'Density_PM', 'IBP_PM', 'FBP_PM', 'tanks_Overall_Status')
    list_editable = ('Suction_Tank_No_PM', 'Blending_Tank_No_PM', 'Blend_Ratio_PM', 'Naphtha_Load_PM', 'LPG_Load_PM',
    'C5_Load_PM', 'C6_Load_PM', 'Naphtha_Heater_PM', 'COT_PM', 'GF_PDI_PM', 'Suc_Pressure_PM', 'Paraffin_PM', 'Olefins_PM',
    'Aromatics_PM', 'Naphthene_PM', 'IN_IP_Ratio_PM', 'Density_PM', 'IBP_PM', 'FBP_PM', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Suction_Tank_No_PM' , '')

class Input_Parameter_UserDefinedAdmin(admin.ModelAdmin):
    list_display = ('id', 'Suction_Tank_No_UD', 'Blending_Tank_No_UD', 'Blend_Ratio_UD', 'Naphtha_Load_UD', 'LPG_Load_UD',
    'C5_Load_UD', 'C6_Load_UD', 'Naphtha_Heater_UD', 'COT_UD', 'GF_PDI_UD', 'Suc_Pressure_UD', 'Paraffin_UD', 'Olefins_UD',
    'Aromatics_UD', 'Naphthene_UD', 'IN_IP_Ratio_UD', 'Density_UD', 'IBP_UD', 'FBP_UD', 'quality_Real')
    list_editable = ('Suction_Tank_No_UD', 'Blending_Tank_No_UD', 'Blend_Ratio_UD', 'Naphtha_Load_UD', 'LPG_Load_UD',
    'C5_Load_UD', 'C6_Load_UD', 'Naphtha_Heater_UD', 'COT_UD', 'GF_PDI_UD', 'Suc_Pressure_UD', 'Paraffin_UD', 'Olefins_UD',
    'Aromatics_UD', 'Naphthene_UD', 'IN_IP_Ratio_UD', 'Density_UD', 'IBP_UD', 'FBP_UD', 'quality_Real')
    list_display_links = ('id', )
    search_fields = ('Suction_Tank_No_UD' , '')


class Output_Parameter_RunningAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ethylene_RN', 'Propylene_RN', 'RPG_RN', 'C4_Mix_RN', 'Fuel_Gas_RN', 'Benzene_RN', 'BD_RN',
    'input_Parameter_Running')
    list_editable = ('Ethylene_RN', 'Propylene_RN', 'RPG_RN', 'C4_Mix_RN', 'Fuel_Gas_RN', 'Benzene_RN', 'BD_RN',
    'input_Parameter_Running')
    list_display_links = ('id', )
    search_fields = ('Ethylene_RN' , '')

class Output_Parameter_BestFitAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ethylene_BF', 'Propylene_BF', 'RPG_BF', 'C4_Mix_BF', 'Fuel_Gas_BF', 'Benzene_BF', 'BD_BF',
    'input_Parameter_BestFit')
    list_editable = ('Ethylene_BF', 'Propylene_BF', 'RPG_BF', 'C4_Mix_BF', 'Fuel_Gas_BF', 'Benzene_BF', 'BD_BF',
    'input_Parameter_BestFit')
    list_display_links = ('id', )
    search_fields = ('Ethylene_BF' , '')

class Output_Parameter_ProfitMaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ethylene_PM', 'Propylene_PM', 'RPG_PM', 'C4_Mix_PM', 'Fuel_Gas_PM', 'Benzene_PM', 'BD_PM',
    'input_Parameter_ProfitMax')
    list_editable = ('Ethylene_PM', 'Propylene_PM', 'RPG_PM', 'C4_Mix_PM', 'Fuel_Gas_PM', 'Benzene_PM', 'BD_PM',
    'input_Parameter_ProfitMax')
    list_display_links = ('id', )
    search_fields = ('Ethylene_PM' , '')

class Output_Parameter_UserDefinedAdmin(admin.ModelAdmin):
    list_display = ('id', 'Ethylene_UD', 'Propylene_UD', 'RPG_UD', 'C4_Mix_UD', 'Fuel_Gas_UD', 'Benzene_UD', 'BD_UD',
    'input_Parameter_UserDefined')
    list_editable = ('Ethylene_UD', 'Propylene_UD', 'RPG_UD', 'C4_Mix_UD', 'Fuel_Gas_UD', 'Benzene_UD', 'BD_UD',
    'input_Parameter_UserDefined')
    list_display_links = ('id', )
    search_fields = ('Ethylene_UD' , '')

class Output_ComparisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Total_Load', 'Naphtha_Load', 'LPG_Load', 'C5_Load', 'C6_Load', 'Naphtha_Heater', 'COT', 'GF_PDI',
    'Suc_Pressure', 'Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Suction_Tank_No', 'Blending_Tank_No', 'Blend_Ratio', 'Ethylene_Actual', 'Propylene_Actual', 'RPG_Actual', 'C4_Mix_Actual',
    'Fuel_Gas_Actual', 'Benzene_Actual', 'BD_Actual', 'Ethylene_Predicted', 'Propylene_Predicted', 'RPG_Predicted',
    'C4_Mix_Predicted', 'Fuel_Gas_Predicted', 'Benzene_Predicted', 'BD_Predicted', 'output_Parameter_Running')
    list_editable = ('Total_Load', 'Naphtha_Load', 'LPG_Load', 'C5_Load', 'C6_Load', 'Naphtha_Heater', 'COT', 'GF_PDI',
    'Suc_Pressure', 'Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Suction_Tank_No', 'Blending_Tank_No', 'Blend_Ratio', 'Ethylene_Actual', 'Propylene_Actual', 'RPG_Actual', 'C4_Mix_Actual',
    'Fuel_Gas_Actual', 'Benzene_Actual', 'BD_Actual', 'Ethylene_Predicted', 'Propylene_Predicted', 'RPG_Predicted',
    'C4_Mix_Predicted', 'Fuel_Gas_Predicted', 'Benzene_Predicted', 'BD_Predicted', 'output_Parameter_Running')
    list_display_links = ('id', )
    search_fields = ('Total_Load' , '')

class New_NaphthaAdmin(admin.ModelAdmin):
    list_display = ('id', 'Transport_Type', 'Date_Transfer_From', 'Date_Transfer_To', 'HOJ', 'Load_Port', 'BL_Quantity',
    'Shore_Quantity', 'Opening_Stock', 'Source', 'PCN_NCU', 'PCN_CPP', 'FGN_CPP', 'CBFS_CPP', 'Vessel_Name',
    'Shortage_Quantity', 'tanks_Overall_Status')
    list_editable = ('Transport_Type', 'Date_Transfer_From', 'Date_Transfer_To', 'HOJ', 'Load_Port', 'BL_Quantity',
    'Shore_Quantity', 'Opening_Stock', 'Source', 'PCN_NCU', 'PCN_CPP', 'FGN_CPP', 'CBFS_CPP', 'Vessel_Name',
    'Shortage_Quantity', 'tanks_Overall_Status')
    list_display_links = ('id', )
    search_fields = ('Date_Transfer_From' , '')

class New_Naphtha_Quality_LabAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'new_Naphtha')
    list_editable = ('Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'new_Naphtha')
    list_display_links = ('id', )
    search_fields = ('Paraffin' , '')

class New_Naphtha_Quality_SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'new_Naphtha')
    list_editable = ('Paraffin', 'Olefins', 'Aromatics', 'Naphthene', 'IN_IP_Ratio', 'Density', 'IBP', 'FBP',
    'Sulfur', 'Colour', 'RVP', 'new_Naphtha')
    list_display_links = ('id', )
    search_fields = ('Paraffin' , '')

class Receipt_TankAdmin(admin.ModelAdmin):
    list_display = ('id', 'Tank_No_1', 'Tank_No_1_Receiving', 'Tank_No_2', 'Tank_No_2_Receiving', 'Tank_No_3',
    'Tank_No_3_Receiving', 'Tank_No_4', 'Tank_No_4_Receiving', 'Tank_No_5', 'Tank_No_5_Receiving', 'new_Naphtha')
    list_editable = ('Tank_No_1', 'Tank_No_1_Receiving', 'Tank_No_2', 'Tank_No_2_Receiving', 'Tank_No_3',
    'Tank_No_3_Receiving', 'Tank_No_4', 'Tank_No_4_Receiving', 'Tank_No_5', 'Tank_No_5_Receiving', 'new_Naphtha')
    list_display_links = ('id', )
    search_fields = ('Tank_No_1' , '')

class Naphtha_Plan_All_MonthsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Month_Year')
    list_editable = ('Month_Year', )
    list_display_links = ('id', )
    search_fields = ('Month_Year' , '')

class Naphtha_Plan_Single_MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'Date', 'Total_Stock', 'Usable_Stock', 'Source', 'Quantity', 'Actual_NCU_TPH', 'Budget_NCU_TPH',
    'Actual_CPP_TPD', 'Budget_CPP_TPD', 'Draft_Level', 'naphtha_Plan_All_Months')
    list_editable = ('Date', 'Total_Stock', 'Usable_Stock', 'Source', 'Quantity', 'Actual_NCU_TPH', 'Budget_NCU_TPH',
    'Actual_CPP_TPD', 'Budget_CPP_TPD', 'Draft_Level', 'naphtha_Plan_All_Months')
    list_display_links = ('id', )
    search_fields = ('Date' , '')

class Naphtha_Plan_SummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Consumption_Total', 'Consumption_NCU', 'Consumption_CPP', 'Procurement_Total', 'Procurement_ADNOC',
    'Procurement_IOC', 'Procurement_BPCL', 'Procurement_HPCL', 'Procurement_KPC', 'Procurement_SPOT', 'Total_Stock',
    'Opening_Stock', 'Closing_Stock', 'Avg_Stock', 'Min_Stock', 'Max_Stock', 'naphtha_Plan_All_Months')
    list_editable = ('Consumption_Total', 'Consumption_NCU', 'Consumption_CPP', 'Procurement_Total', 'Procurement_ADNOC',
    'Procurement_IOC', 'Procurement_BPCL', 'Procurement_HPCL', 'Procurement_KPC', 'Procurement_SPOT', 'Total_Stock',
    'Opening_Stock', 'Closing_Stock', 'Avg_Stock', 'Min_Stock', 'Max_Stock', 'naphtha_Plan_All_Months')
    list_display_links = ('id', )
    search_fields = ('Consumption_Total' , '')

class LoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'Username', 'Password')
    list_editable = ('Username', 'Password')
    list_display_links = ('id', )
    search_fields = ('Username' , '')

# Register your models here.
admin.site.register(Tanks_Overall_Status, Tanks_Overall_StatusAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(Quality_Avg, Quality_AvgAdmin)
admin.site.register(Quality_Real, Quality_RealAdmin)
admin.site.register(Quality_NIR_Actual, Quality_NIR_ActualAdmin)
admin.site.register(Quality_NIR_Pred, Quality_NIR_PredAdmin)
admin.site.register(Plant_Constraints, Plant_ConstraintsAdmin)
admin.site.register(Input_Parameter_Running, Input_Parameter_RunningAdmin)
admin.site.register(Input_Parameter_BestFit, Input_Parameter_BestFitAdmin)
admin.site.register(Input_Parameter_ProfitMax, Input_Parameter_ProfitMaxAdmin)
admin.site.register(Input_Parameter_UserDefined, Input_Parameter_UserDefinedAdmin)
admin.site.register(Output_Parameter_Running, Output_Parameter_RunningAdmin)
admin.site.register(Output_Parameter_BestFit, Output_Parameter_BestFitAdmin)
admin.site.register(Output_Parameter_ProfitMax, Output_Parameter_ProfitMaxAdmin)
admin.site.register(Output_Parameter_UserDefined, Output_Parameter_UserDefinedAdmin)
admin.site.register(New_Naphtha, New_NaphthaAdmin)
admin.site.register(Receipt_Tank, Receipt_TankAdmin)
admin.site.register(New_Naphtha_Quality_Supplier, New_Naphtha_Quality_SupplierAdmin)
admin.site.register(New_Naphtha_Quality_Lab, New_Naphtha_Quality_LabAdmin)
admin.site.register(Naphtha_Plan_All_Months, Naphtha_Plan_All_MonthsAdmin)
admin.site.register(Naphtha_Plan_Single_Month, Naphtha_Plan_Single_MonthAdmin)
admin.site.register(Naphtha_Plan_Summary, Naphtha_Plan_SummaryAdmin)
admin.site.register(Next_Hour_Selection, Next_Hour_SelectionAdmin)
admin.site.register(Model_Output_Parameter_Running, Model_Output_Parameter_RunningAdmin)
admin.site.register(Output_Comparision, Output_ComparisionAdmin)
admin.site.register(Login, LoginAdmin)


