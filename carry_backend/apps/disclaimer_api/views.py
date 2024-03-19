from .serializers import DisclaimerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Disclamer
from apps.user_api.models import CarryUser
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
def GetLastDisclaimer():
    disclaimer = Disclamer.objects.last()
    return disclaimer

class ReturnLastDisclaimer(APIView):
    def get(self, request, format=None):
        serializer = DisclaimerSerializer(GetLastDisclaimer(), many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ReturnAllDisclaimers():
    pass

class SignDisclaimer(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self,request):
        if self._sign_disclaimer(request):
            return Response(data={'is_signed':True}, status=status.HTTP_200_OK)
        else:
            return Response(data={'is_signed':False}, status=status.HTTP_418_IM_A_TEAPOT)
    
    def _sign_disclaimer(self, request):
        current_disclaimer = GetLastDisclaimer()
        if current_disclaimer.pk == int(request.data['data']['id']):
            try:
                user_obj = CarryUser.objects.get(pk=request.user.pk)
                user_obj.disclaimer_id=current_disclaimer
                user_obj.date_disclaimer_signed=datetime.now()
                user_obj.save()
                return True
            except:
                return False
        return False