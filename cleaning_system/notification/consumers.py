from  channels.generic.websocket  import AsyncWebsocketConsumer
import  json
from company.serializers   import CompanySerializer
from django.http import JsonResponse
from  .models  import  Notification
from asgiref.sync import sync_to_async
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            self.scope['url_route']['kwargs']['uuid'],
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.scope['url_route']['kwargs']['uuid'],
            self.channel_name
        )
   
  

    async def  send_notification(self,event):
        id=event['id']
        name=event['name']
        description=event['description']
        notification=event['notification']
        await  self.send(text_data=json.dumps({'id':id,'name':name,'description':description,
        'notification':notification}))
    

   