# Generated by Django 4.1.2 on 2022-10-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_remove_profile_album_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='photo_url',
            field=models.CharField(default='http://dalelyles.com/musicmp3s/no_cover.jpg', max_length=200),
        ),
    ]
