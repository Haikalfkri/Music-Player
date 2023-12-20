from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    audio_path = models.FileField(upload_to="song/")
    
    def __str__(self):
        return self.title
    
    
class Playlist(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title