from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints, Quality_Real, Input_Parameter_BestFit,Input_Parameter_ProfitMax

import numpy
import random


class Profit_Max_Model():
    def profit_max_model_recommendations(instance):
        level = [0] * 5
        paraffin = [0] * 5
        aromatics = [0] * 5
        density = [0] * 5
        inipratio = [0] * 5
        recommendations = [0] * 19
        output = [0] * 7
        parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]


        for i in range(0,5):
            tank_obj = Tank.objects.filter(tanks_Overall_Status = parent_obj, Tank_No = i+1).get()
            level[i] = tank_obj.Level
            paraffin[i] = Quality_Real.objects.filter(tank=tank_obj).get().Paraffin_Real
            aromatics[i] = Quality_Real.objects.filter(tank=tank_obj).get().Aromatics_Real
            density[i] = Quality_Real.objects.filter(tank=tank_obj).get().Density_Real
            inipratio[i] = Quality_Real.objects.filter(tank=tank_obj).get().IN_IP_Ratio_Real

        # model .......
        # 
        recommendations[0] = 4
        recommendations[1] = 5
        recommendations[2] = .75

        for i in range(3,19):
            recommendations[i] = random.randint(10,50)

        return recommendations


    def profit_max_model_output(instance):

        output = [0] * 7
        parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
        inputparameters = Input_Parameter_ProfitMax.objects.filter(tanks_Overall_Status = parent_obj).get()

        # model .......
        # 
        output = random.sample(range(10, 100), 7)
        return output


