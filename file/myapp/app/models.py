from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=20)
    email = models.TextField()
    unique = models.UUIDField(primary_key=True, help_text='Unique ID for this person', null=True)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class randompass(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this person')
    person = models.ForeignKey('post', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        return f'{self.id} ({self.person.title})'
