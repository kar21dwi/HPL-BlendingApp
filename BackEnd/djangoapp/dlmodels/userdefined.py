from djangoapp.api.models import Tanks_Overall_Status,Tank,Quality_Avg, New_Naphtha, Receipt_Tank
from djangoapp.api.models import New_Naphtha_Quality_Lab, Quality_NIR_Actual,Plant_Constraints, Quality_Real, Input_Parameter_BestFit,Input_Parameter_ProfitMax,Input_Parameter_UserDefined

import numpy
import random

class User_Defined_Model():

    def user_defined_model_output(obj):

        output = [0] * 7
        inputparameters = Input_Parameter_UserDefined.objects.filter(pk = obj.id).get()
        print ("%%%%%%%%%%%%%%"+str(inputparameters))

        # model .......
        # 
        output = random.sample(range(10, 100), 7)
        return output


