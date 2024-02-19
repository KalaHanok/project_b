from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from .utils import generateOtp,sendMsg,addVerifiedNumber
from datetime import datetime,timedelta
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
User=get_user_model()
class OTPGeneration(APIView):
    def post(self, request):
        mobile=request.data.get('mobile',None)
        if mobile is not None:
            user=User.objects.filter(mobile=mobile)
            if len(user)==0:
                user = User.objects.create_user(mobile=mobile)
                if user is None:
                    return Response({'msg':'problem in creating a user'})
                #adding number to twilio 
                # addVerifiedNumber(mobile,user.id)
            else:
                user=user[0]
            otp=generateOtp()
            # sendMsg(mobile,otp)
            user.otp=otp
            user.otp_expiry=datetime.now()+timedelta(minutes=1)
            user.save()
            print(otp)
            return Response({'msg':'otp is sent successfully'})
        else:
            return Response({'msg':'required a field "mobile"'})
        
class TokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        otp = request.data.get('otp')
        user = authenticate(mobile=mobile, otp=otp)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid opt or otp time expired'}, status=status.HTTP_401_UNAUTHORIZED)