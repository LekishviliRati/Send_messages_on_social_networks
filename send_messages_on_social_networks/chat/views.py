from django.shortcuts import render
from .models import Message


def home(request):
    return render(request, 'home.html')


def list_message(request):
    message = Message.objects.all()
    return render(request, 'list_messages.html', {'messages': message})
