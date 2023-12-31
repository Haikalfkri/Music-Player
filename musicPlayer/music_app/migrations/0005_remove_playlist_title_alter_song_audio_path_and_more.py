# Generated by Django 5.0 on 2023-12-21 03:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("music_app", "0004_alter_song_audio_path_alter_song_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playlist",
            name="title",
        ),
        migrations.AlterField(
            model_name="song",
            name="audio_path",
            field=models.FileField(upload_to="song/"),
        ),
        migrations.AlterField(
            model_name="song",
            name="image",
            field=models.ImageField(upload_to="images/"),
        ),
    ]
