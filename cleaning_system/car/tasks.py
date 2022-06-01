from  celery  import shared_task
from .models  import Car

import random
import string
from  random  import  randint

@shared_task
def   create_car():
    letters = string.ascii_uppercase
    name=''.join(random.choice(letters) for i in range(10))
    description=''.join(random.choice(letters) for i in range(30))
    speed=randint(100,300)
    Car.objects.create(name=name,description=description, speed=speed)
