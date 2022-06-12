from django.db import models
from  django.contrib.auth import get_user_model
User=get_user_model()
from  company.models  import Company

class  Notification(models.Model):
    class Status(models.IntegerChoices):
        READ=1
        NOT_READ=0
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    status=models.IntegerField(choices=Status.choices,default=Status.NOT_READ)


