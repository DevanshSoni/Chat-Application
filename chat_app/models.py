from django.db import models
from django.db.models.signals import post_save, pre_save

# Create your models here.

class notify(models.Model):
    title = models.TextField()
    notification = models.TextField()

def show_notify(sender, instance, **kwargs):
    print("Something is there")
    print(sender)
    print(instance)

post_save.connect(show_notify, sender = notify)