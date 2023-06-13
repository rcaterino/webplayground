from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.thread_id = self.scope['url_route']['kwargs']['thread_id']
        self.room_group_name = 'thread_%s' % self.thread_id

        # Unirse al grupo de la conversación
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo de la conversación
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recibir mensaje desde WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = data['user']

        # Enviar mensaje al grupo de la conversación
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    # Recibir mensaje del grupo de la conversación
    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        # Enviar mensaje al WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))
