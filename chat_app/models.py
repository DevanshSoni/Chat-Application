from django.db import models
from django.db.models.signals import post_save, pre_save
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField()

class notify(models.Model):
    client_user_id = models.TextField()
    host_user_id = models.TextField() 
    message_received = models.TextField()

def show_notify(sender, instance, **kwargs):    #---> Receiver Function
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "group_name",
        {
            'type': 'send_message',
            'text': {
                        'Message': "You have a new Message",
                    }
        }
    )

post_save.connect(show_notify, sender = notify)