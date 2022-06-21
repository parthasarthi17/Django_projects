from django.db import models
from ckeditor.fields import RichTextField



class User(models.Model):
    user_name = models.CharField(max_length=70)
    pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Editor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
