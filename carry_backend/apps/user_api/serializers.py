from rest_framework import serializers
from .models import CarryUser
#Set-ExecutionPolicy Unrestricted -Scope Process    
class CarryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarryUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("call me?")
        user = CarryUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            )
        user.set_password(validated_data['password']) 
        user.save()
        return user