# Generated by Django 3.2.9 on 2021-11-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0007_alter_person_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='emailid',
            field=models.TextField(default='Emailid@server.com'),
        ),
        migrations.AddField(
            model_name='person',
            name='qwertypass',
            field=models.TextField(default='Passwrod12345!@'),
        ),
    ]