# Generated by Django 3.2.9 on 2021-11-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0002_auto_20211115_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('otp', models.UUIDField(help_text='Unique ID for this person', primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='messaging',
        ),
    ]
