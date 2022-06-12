from django.db import models
from  django.contrib.auth import get_user_model
from  company.models import Company
User=get_user_model()

class  Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateTimeField(auto_now=True)

