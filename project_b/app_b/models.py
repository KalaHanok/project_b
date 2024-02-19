from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils import timezone
# Create your models here.
class MyUserModel(AbstractUser):
    mobile=models.CharField(max_length=15,unique=True)
    otp=models.CharField(max_length=6)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD='mobile'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()
    def __str__(self):
        return self.mobile
    def is_otp_valid(self):
        return self.otp_expiry is not None and self.otp_expiry > timezone.now()
