# Generated by Django 4.1 on 2022-12-03 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='eventName',
        ),
    ]
