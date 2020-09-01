from django.db import models
from django.db.models.signals import post_save, pre_save

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.TextField()

class notify(models.Model):
    client_user_id = models.TextField()
    host_user_id = models.TextField() 
    message_received = models.TextField()

def show_notify(sender, instance, **kwargs):    #---> Receiver Function
    print("Something is here to show")
    print(sender)
    print(kwargs)
    # print(instance.client_user_id,instance.host_user_id,instance.message)


post_save.connect(show_notify, sender = notify)