# Generated by Django 3.2.9 on 2021-11-10 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0003_auto_20211030_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geeksmodel',
            name='created',
        ),
        migrations.RemoveField(
            model_name='geeksmodel',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='geeksmodel',
            name='updated',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
