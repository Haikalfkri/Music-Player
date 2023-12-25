from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="music"),
    path("playlist/", views.playlist, name="playlist"),
    path("add-to-playlist/<int:song_id>/", views.addToPlaylist, name="add-to-playlist"),
    path('delete-playlist/<int:song_id>/', views.deletePlaylist, name="delete-playlist"),
]
