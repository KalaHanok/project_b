from django.contrib.auth.backends import BaseBackend
from .models import MyUserModel
from django.utils import timezone

class CustomMobileOTPBackend(BaseBackend):
    def authenticate(self, request, mobile=None, otp=None, **kwargs):
        try:
            user = MyUserModel.objects.get(mobile=mobile)
            if user.otp == otp and user.is_otp_valid():
                return user
            else:
                return None
        except MyUserModel.DoesNotExist:
            return None