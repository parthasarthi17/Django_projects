# Generated by Django 3.2.9 on 2021-11-09 11:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211109_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='randompass',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this person', primary_key=True, serialize=False),
        ),
    ]