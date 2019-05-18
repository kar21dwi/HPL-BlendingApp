from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tank
from .models import Login

#Tank Class
class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('id', 'Avg_Quality', 'Real_Time_Quality', 'NIR_Reading')

#Login Class
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'Username', 'Password')


