from django.db import models
import  datetime
from  service_type.models  import Service
from django.utils import timezone
class  Company(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    operation_city=models.CharField(max_length=50)
    date_foundation=models.DateField( null=False, blank=False, auto_now=True)
    services=models.ManyToManyField(Service)

    def  __str__(self):
        return  self.title
