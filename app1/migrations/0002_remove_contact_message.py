# Generated by Django 3.2 on 2021-04-16 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='Message',
        ),
    ]
