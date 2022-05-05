from django.db import models
from django.contrib.auth.models import User
from  cleaning_company.models import  Company
from service_type.models  import Service
class  Request(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    cleaning_type=models.ForeignKey(Service, on_delete=models.CASCADE)
    location=models.CharField(max_length=255)
    area=models.DecimalField(decimal_places=2,max_digits=6)
    hourse=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=6)
