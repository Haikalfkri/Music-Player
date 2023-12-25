from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    audio_path = models.FileField(upload_to="song/")
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url  
    
    @property
    def audioURL(self):
        try:
            url = self.audio_path.url
        except:
            url = ''
        return url
    
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song, blank=True)
    
    def __str__(self):
        return self.user.username