from django.db import models
from django.utils import timezone
#import uuid

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=20)
    email = models.TextField()


    def __str__(self):
        return self.title
