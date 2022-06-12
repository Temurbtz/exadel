from django.db import models
from  company.models import  Company
from django.http import Http404
from  django.contrib.auth import get_user_model
User=get_user_model()

class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category

        

class  Service(models.Model):
    class Unit(models.TextChoices):
        SQUARE_METER='per meter  square'
        HOUR='per  hour'
        KILOGRAMM='per kg'
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    measurement_unit=models.CharField(choices=Unit.choices,max_length=30)
    per_unit_price=models.FloatField()
    company=models.ForeignKey(Company, on_delete=models.CASCADE, related_name='services', blank=True, editable=False)
    descriptive_picture=models.ImageField(blank=True,null=True)
  

    def  __str__(self):
        return  self.category



