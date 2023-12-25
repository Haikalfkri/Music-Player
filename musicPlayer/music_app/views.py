from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
def index(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, "music_app/music.html", context=context)

def playlist(request):
    user = request.user
    playlists = Playlist.objects.filter(user=user)
    context = {
        'playlists': playlists
    }
    return render(request, "music_app/playlist.html", context=context)


def addToPlaylist(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    playlist, created = Playlist.objects.get_or_create(user=request.user)
    playlist.songs.add(song)
    return JsonResponse({'message': "Song added to playlist succesfully"})


def deletePlaylist(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    playlist = Playlist.objects.filter(user=request.user).first()
    if playlist:
        playlist.songs.remove(song)
        return JsonResponse({'message': 'Music successfully deleted'})
    else:
        return JsonResponse({'message': 'Playlist not found'}, status=404)