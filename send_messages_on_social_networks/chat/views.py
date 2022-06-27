from django.shortcuts import render
from .models import Message


def list_message(request):
    message = Message.objects.all()
    return render(request, 'list_messages.html', {'messages': message})
