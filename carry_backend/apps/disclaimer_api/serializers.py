from rest_framework import serializers
from .models import Disclamer
#Set-ExecutionPolicy Unrestricted -Scope Process    
class DisclaimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disclamer
        fields = ['id', 'description', 'published_date']