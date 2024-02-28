from django.shortcuts import render
from rest_framework import generics
from .serializers import DisclaimerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Disclamer
# Create your views here.
class ReturnLastDisclaimer(APIView):
    def get(self, request, format=None):
        disclaimer = Disclamer.objects.last()
        serializer = DisclaimerSerializer(disclaimer, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ReturnAllDisclaimers():
    pass