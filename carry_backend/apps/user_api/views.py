from .models import CarryUser
from rest_framework.generics import CreateAPIView
from .serializers import CarryUserSerializer
# Create your views here.
class RegisterUser(CreateAPIView):
    serializer_class = CarryUserSerializer
