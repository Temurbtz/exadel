from django.db import models
from  cleaning_company.models  import Company
from django.contrib.auth.models import User
class  Review(models.Model):
    review=models.TextField()
    RATING_CHOICES=(
      
        ('VERY_BAD',1),
        ('BAD',2),
      ('MEDIUM',3),
      ('GOOD',4),
      ('VERY_GOOD',5),
    )
     
    rating=models.IntegerField(choices=RATING_CHOICES)
    company=models.ManyToManyField(Company)
    user=models.ManyToManyField(User)

