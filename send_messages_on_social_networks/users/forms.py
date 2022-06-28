from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'password']
