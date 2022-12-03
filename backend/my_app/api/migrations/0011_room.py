# Generated by Django 4.1 on 2022-12-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_name_event_eventname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferences', models.ManyToManyField(related_name='rooms', to='api.preference')),
                ('tags', models.ManyToManyField(related_name='rooms', to='api.tag')),
            ],
        ),
    ]