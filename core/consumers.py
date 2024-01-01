import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

"""
A consumer is an abstraction of a channel in the form of a class, this class implements methods 
that will be responsible for handling the events of our users. There are also synchronous and 
asynchronous consumers that handle low-level Python code for you.

In this case we are not using WebSocket to send an specific message, we just want to
establish a communication with all consumers in order to automatically update
first to serve turns table every time a service desk user call for a new turn to serve
"""


class TurnWebSocket(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("turnow", self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("turnow", self.channel_name)

    """
    Now, every time you see that we receive a message in a consumer, it will call the group_send 
    method of the channel layer to which it belongs, which will be in charge of sending the data, 
    in the form of a dictionary, automatically to all the active members of the group "turnow.

    The type key will tell the consumer which method to use. The syntax is to replace the period 
    with an underscore. That is, the type turnow.message will execute the turnow_message method of 
    each consumer that receives it.
    """

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            "turnow",
            {
                "type": "turnow.message",
                "text": text_data,
            },
        )

    def turnow_message(self, event):
        self.send(text_data=event["text"])
