from django.db import models
from  company.models import Company
from  service.models  import Service
from  django.contrib.auth import get_user_model
User=get_user_model()

class Request(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, editable=False)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,  editable=False)
    service=models.ForeignKey(Service,on_delete=models.CASCADE)
    location=models.TextField()
    measurement_unit_count=models.FloatField()
    total_cost=models.FloatField()
    date=models.DateTimeField(auto_now=True)

