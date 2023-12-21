from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(request, "music_app/music.html", context=context)



def playlist(request):
    context = {}
    return render(request, "music_app/playlist.html", context=context)
