from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "music_app/music.html", context=context)


def playlist(request):
    context = {}
    return render(request, "music_app/playlist.html", context=context)
