from django.db import models
from users.models import User


class Message(models.Model):
    content = models.TextField(default="aucun messsage")
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)



