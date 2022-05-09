from datetime import datetime
from django.db import models

class  Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=4)
   


    
   
