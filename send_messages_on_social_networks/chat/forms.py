from .models import Message
from django.forms import ModelForm


class MessageRegisterForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content']
