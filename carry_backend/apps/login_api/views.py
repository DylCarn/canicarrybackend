from django.contrib.auth.models import Group, User
from apps.login_api.serializers import UserSerializer
from rest_framework import generics
class UserViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

    class CreateUser():
        pass

    class AuthenticateUser():
        pass