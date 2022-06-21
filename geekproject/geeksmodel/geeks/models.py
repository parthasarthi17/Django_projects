from django.db import models
from django.conf import settings
from django.urls import reverse


class GeeksModel(models.Model):

    title = models.CharField(max_length=100)
    descrption = models.TextField()

    def __str__(self):
        return self.title
