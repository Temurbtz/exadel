


from  celery  import shared_task
from  channels.layers  import get_channel_layer
from  asgiref.sync  import async_to_sync

from   django.contrib.auth  import   get_user_model
User=get_user_model()

from  company.models  import Company
from random import randint

from  .models  import  Notification

from  request.models  import Request
from  service.models import Service
from datetime import date, timedelta


channel_layer=get_channel_layer()
@shared_task
def   send_notifications():
    Notification.objects.filter(status=1).delete()
    some_day_last_week = date.today() - timedelta(days=7)
    request_queryset=Request.objects.filter(date__gt= some_day_last_week)
    for  item in  request_queryset:
        services=Service.objects.filter(category=item.service.category)
        value=randint(1,services.count()-1)
        company=services[value].company
        if  item.company!=company:
            notification=Notification.objects.create(user=item.user, company=company)
            async_to_sync(channel_layer.group_send)(
                str(item.user.uuid),
            {'type':'send_notification',
            'id': company.id,
            'name':company.name,
            'description':company.description,
            'notification':notification.id
                            })


            
        
            
