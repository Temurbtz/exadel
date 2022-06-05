import  os
from  celery  import  Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','cleaning_system.settings')

app=Celery('cleaning_system')
app.config_from_object('django.conf:settings',  namespace='CELERY')


app.conf.beat_schedule={
    'create_car':{
        'task':'car.tasks.create_car',
        'schedule':30.0
    }
}


app.autodiscover_tasks()
