from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints, Quality_Real, Input_Parameter_BestFit

import numpy
import random

class Best_Fit_Model():
    def best_fit_model_recommendations(instance):
        plantconstraints = [0] * 7
        level = [0] * 5
        paraffin = [0] * 5
        aromatics = [0] * 5
        density = [0] * 5
        inipratio = [0] * 5
        recommendations = [0] * 19
        output = [0] * 7
        parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
        
        plantconstraint = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()
        plantconstraints[1] = plantconstraint.Max_Ethylene
        plantconstraints[2] = plantconstraint.Max_Propylene
        plantconstraints[3] = plantconstraint.Max_RPG
        plantconstraints[4] = plantconstraint.Max_C4_Mix
        plantconstraints[4] = plantconstraint.Max_Fuel_Gas
        plantconstraints[4] = plantconstraint.Max_Benzene
        plantconstraints[4] = plantconstraint.Max_BD

        for i in range(0,5):
            tank_obj = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = i+1).get()
            level[i] = tank_obj.Level
            paraffin[i] = Quality_Real.objects.filter(tank=tank_obj).get().Paraffin_Real
            aromatics[i] = Quality_Real.objects.filter(tank=tank_obj).get().Aromatics_Real
            density[i] = Quality_Real.objects.filter(tank=tank_obj).get().Density_Real
            inipratio[i] = Quality_Real.objects.filter(tank=tank_obj).get().IN_IP_Ratio_Real

        # model .......
        # 
        recommendations[0] = 2
        recommendations[1] = 3
        recommendations[2] = .8

        return recommendations


    def best_fit_model_output(instance):

        output = [0] * 7
        parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
        plantconstraint = Plant_Constraints.objects.filter(tanks_Overall_Status = parent_obj).get()
        inputparameters = Input_Parameter_BestFit.objects.filter(plant_Constraints = plantconstraint).get()

        # model .......
        # 
        output = random.sample(range(10, 100), 7)
        return output


