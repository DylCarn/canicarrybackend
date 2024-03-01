from .models import CarryUser
from rest_framework.generics import CreateAPIView
from .serializers import CarryUserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.
class RegisterUser(CreateAPIView):
    serializer_class = CarryUserSerializer
    user_obj = None
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        print(self.user_obj.pk)
        headers = self.get_success_headers(serializer.data)
        token = self.returntoken()
        print(token)
        print(serializer.data)
        return Response(data={'user':serializer.data, 'token': token}, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        obj = serializer.save()
        self.user_obj = obj
    
    def returntoken(self):
        token = Token.objects.get_or_create(user=self.user_obj)[0]
        return str(token)