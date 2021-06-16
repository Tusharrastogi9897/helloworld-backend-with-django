"""
We are creating this consumer for testing the tutorial
https://channels.readthedocs.io/en/stable/tutorial/part_2.html

"""
import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

class GlobalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'global'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "global",
            {
                "type": "chat_message",
                "text": text_data,
            },
        )

    async def chat_message(self, event):
        await self.send(text_data=event["text"])

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
