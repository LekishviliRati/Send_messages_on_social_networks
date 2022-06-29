from django.db import models
from users.models import User


class Message(models.Model):
    content = models.TextField(default="...")
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.content
