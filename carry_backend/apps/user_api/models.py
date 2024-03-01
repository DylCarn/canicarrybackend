from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.disclaimer_api.models import Disclamer
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
# Create your models here.        
class CarryUser(AbstractUser):
    disclaimer = models.ForeignKey(Disclamer, on_delete=models.PROTECT, null=True, blank=True)
    date_disclaimer_signed = models.DateField(blank=True, null=True)
