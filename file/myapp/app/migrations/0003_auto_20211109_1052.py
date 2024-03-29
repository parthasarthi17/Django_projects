# Generated by Django 3.2.9 on 2021-11-09 10:52

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211109_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='unique',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this person', primary_key=True, serialize=False),
        ),
    ]
