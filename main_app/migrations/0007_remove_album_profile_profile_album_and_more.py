# Generated by Django 4.1.2 on 2022-10-12 01:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_album_track_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='album',
            field=models.ManyToManyField(to='main_app.album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='track_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]
