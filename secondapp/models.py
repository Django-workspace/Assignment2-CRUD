from django.db import models

# Create your models here.
class secondapp(models.Model):
    type=models.CharField(max_length=10)
    