from django.contrib import admin

from .models import Tanks_Overall_Status,Tank,Quality_Avg,Quality_Real,Quality_NIR_Actual,Quality_NIR_Pred,Plant_Constraints,Login,Sample,sum

# Register your models here.
admin.site.register(Tanks_Overall_Status)
admin.site.register(Tank)
admin.site.register(Quality_Avg)
admin.site.register(Quality_Real)
admin.site.register(Quality_NIR_Actual)
admin.site.register(Quality_NIR_Pred)
admin.site.register(Plant_Constraints)
admin.site.register(Login)
admin.site.register(Sample)
admin.site.register(sum)

