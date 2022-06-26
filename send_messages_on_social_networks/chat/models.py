from django.db import models


class Message(models.Model):
    content = models.TextField(default="aucun messsage")
    publication_date = models.DateTimeField(auto_now_add=True)


