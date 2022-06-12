from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


       



class  Company(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    date_foundation=models.DateField(auto_now=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    logo=models.ImageField(blank=True, null=True)
    

    def  __str__(self):
        return  self.name




class Rating(models.Model):
    class Stars(models.IntegerChoices):
        ONE=1
        TWO=2
        THREE=3
        FOUR=4
        FIVE=5
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    rating=models.IntegerField(choices=Stars.choices)




