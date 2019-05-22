from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Login





#Login Class
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'Username', 'Password')


