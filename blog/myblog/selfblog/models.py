from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bod = models.TextField()

    def __str__(abc):
        return str(abc.title) + '|' + str(abc.author)
