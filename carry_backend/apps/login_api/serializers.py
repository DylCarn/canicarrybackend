from django.contrib.auth.models import User
from rest_framework import serializers

#Set-ExecutionPolicy Unrestricted -Scope Process    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'password']