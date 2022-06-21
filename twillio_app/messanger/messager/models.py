from django.db import models
from twilio.rest import Client
import uuid

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    emailid = models.EmailField(max_length=80)
    qwertypass = models.CharField(max_length=20)
    unique = models.TextField(primary_key=True, help_text='Unique ID for this person')

    def __str__(self):
        return str(self.number)

    def save(self, *args, **kwargs):
        account_sid = "AC13925746a3d2d7a3993719c04e00ec5d"
        auth_token = 'ed090b2d2dcf91ca19d010b88f2dbfa8'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body=f'This is your OTP for {self.name} : {self.unique}',
                                    from_='+18646060883',
                                    to=f'+91{self.number}'
                                )
        print(message.sid)


        return super().save(*args, **kwargs)
