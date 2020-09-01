from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.dispatch import receiver
from django.core.signals import request_finished
# Create your views here.
import json


def index(request):
    return render(request, 'chat/index.html',{})

# @receiver(request_finished)
# def post_request_receiver(sender, **kwargs):
#     print("request_finished")

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })