from django.db import models
from django.contrib.auth.models import AbstractUser


# Created custom user in case we need add to add extra fields to users
class User(AbstractUser):
    age = models.CharField(max_length=3, default=None)
