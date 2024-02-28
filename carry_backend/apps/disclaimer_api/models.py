from django.db import models

# Create your models here.
class Disclamer(models.Model):
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
#this would be in user_api app
#class User(user override things):
    #disclaimer_signed - fkey to disclaimer pk