# Generated by Django 2.2 on 2019-04-26 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='hits',
            new_name='visits',
        ),
    ]