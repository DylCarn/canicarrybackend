from django.db import models

# Create your models here.
class Disclamer(models.Model):
    description = models.TextField()
    published_date = models.DateField(auto_now_add=True)
