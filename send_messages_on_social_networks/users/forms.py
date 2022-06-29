from .models import User
from django.forms import ModelForm


class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'password']
