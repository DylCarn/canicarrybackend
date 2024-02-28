from django.db import models

# Create your models here.
class Disclamer(models.model):
    description = models.TextField(max_length=1078)
    published_date = models.DateField(auto_now_add=True)
#this would be in user_api app
#class User(user override things):
    #disclaimer_signed - fkey to disclaimer pk