from django.shortcuts import render
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
        if form.is_valid():
            content = form.cleaned_data['content']
            send_content_to_discord = SendMessageToDiscord(content)
            form.instance.author = request.user
            form.save()
            form = MessageRegisterForm()
            user = request.user.id
            message = Message.objects.filter(author_id=user)
            return render(request, 'list_messages.html', {'messages': message, 'form': form})

