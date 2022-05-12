from django.db import models
from  cleaning_company.models  import Company
from django.contrib.auth.models import User
class  Review(models.Model):
    class Rating(models.TextChoices):
        VERY_BAD="Very bad"
        BAD="Bad"
        MEDIUM="Medium"
        GOOD="Good"
        VERY_GOOD="Very  good"
    review=models.TextField()
    rating=models.CharField(choices=Rating.choices,max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    user=models.ForeignKey(User,default=1, on_delete=models.CASCADE)

