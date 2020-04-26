from django.db import models


class User(models.Model):
    name = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=14)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
