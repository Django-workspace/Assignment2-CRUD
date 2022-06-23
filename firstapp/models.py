from django.db import models

# Create your models here.
class FirstModel(models.Model):
    name=models.CharField(max_length=10)
    age=models.PositiveBigIntegerField()
    created_on=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 
        
