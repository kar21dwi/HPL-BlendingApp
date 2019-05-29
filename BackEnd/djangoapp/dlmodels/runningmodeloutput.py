from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints, Quality_Real, Input_Parameter_BestFit,Input_Parameter_ProfitMax, Input_Parameter_Running

import numpy
import random


class Running_Model_Output():

    def running_model_output(instance):
    
        output = [0] * 7
        parent_obj = Tanks_Overall_Status.objects.all().order_by('-id')[0]
        inputparameters = Input_Parameter_Running.objects.filter(tanks_Overall_Status = parent_obj).get()
        suctiontank =  parent_obj.Suction_Tank_No_RN
        blendingtank = parent_obj.Blending_Tank_No_RN
        br = parent_obj.Blend_Ratio_RN

        # model .......
        # 

        output = random.sample(range(10, 100), 7)
        return output


