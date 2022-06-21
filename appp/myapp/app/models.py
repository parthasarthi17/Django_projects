from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()


    def __str__(self):
        return self.title

class list(models.Model):
    head = models.CharField(max_length=20)
    descr = models.TextField()
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
