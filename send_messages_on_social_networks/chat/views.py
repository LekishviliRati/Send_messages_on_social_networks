import json

from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageRegisterForm
from .discord_chat import SendMessageToDiscord


def home(request):
    return render(request, 'home.html')


def list_message(request):
    if request.method == "GET":
        form = MessageRegisterForm()
        return render(request, 'list_messages.html', locals())
    elif request.method == "POST":
        form = MessageRegisterForm(request.POST)
        message = Message.objects.all()
        if form.is_valid():
            content = form.cleaned_data['content']
            send_content_to_discord = SendMessageToDiscord(content)
            form.save()
            return render(request, 'list_messages.html', {'messages': message, 'form': form})
            # return redirect("list_message")

