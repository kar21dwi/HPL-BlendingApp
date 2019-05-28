from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints

import numpy


class Quality_Real_Model():
    def quality_real_model(instance):
        old_obj_tankoverallstatus = Tanks_Overall_Status.objects.all().order_by('-id')[1]
        level = [0] * 5
        paraffin = [0] * 5
        aromatics = [0] * 5
        density = [0] * 5
        inipratio = [0] * 5
        output = numpy.zeros((5, 4))

        for i in range(0,5):
            old_obj_tank = Tank.objects.filter(tanks_Overall_Status = old_obj_tankoverallstatus, Tank_No = i+1).get()
            level[i] = old_obj_tank.Level
            paraffin[i] = Quality_Avg.objects.filter(tank=old_obj_tank).get().Paraffin
            aromatics[i] = Quality_Avg.objects.filter(tank=old_obj_tank).get().Aromatics
            density[i] = Quality_Avg.objects.filter(tank=old_obj_tank).get().Density
            inipratio[i] = Quality_Avg.objects.filter(tank=old_obj_tank).get().IN_IP_Ratio
        

        #model = inputs ----- processing 
        #
        # 
        # 
        
        return output