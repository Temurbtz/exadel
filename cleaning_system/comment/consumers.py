import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


from django.contrib.auth import get_user_model
from pyparsing import empty

User = get_user_model()
from company.models import  Company
from  comment.models  import Comment

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['company_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        comment = data['comment']
        user_uuid = data['user_uuid']
        
        saved=await self.save_message(user_uuid, int(self.scope['url_route']['kwargs']['company_id'] ),comment)
        if  saved:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'comment_message',
                    'comment': comment,
                    'user_uuid': user_uuid,
                   
                }
            )
        else:
            await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'not_found',
                'message': "Error!",
               
            }
            )

    
    async def comment_message(self, event):
        comment = event['comment']
        user_uuid = event['user_uuid']
       
        await self.send(text_data=json.dumps({
            'comment': comment,
            'user_uuid': user_uuid,
           
        }))

    @sync_to_async
    def save_message(self, user_uuid, company_id, comment):
        user = User.objects.filter(uuid=user_uuid)
        company = Company.objects.filter(pk=company_id)
        if(user.exists()  and company.exists()):
            Comment.objects.create(user=user[0], company=company[0], text=comment)
            return  True
        else:
            return False
    async def not_found(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message,
        }))
