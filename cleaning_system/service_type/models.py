from django.db import models
from django.forms import CharField

class  Service(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=6)

    def  __str__(self):
        return  self.title
