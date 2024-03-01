from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.disclaimer_api.models import Disclamer
# Create your models here.
class CarryUser(AbstractUser):
    disclaimer = models.ForeignKey(Disclamer, on_delete=models.PROTECT, null=True, blank=True)
    date_disclaimer_signed = models.DateField(blank=True, null=True)
