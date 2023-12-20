from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="music"),
    path("playlist", views.playlist, name="playlist"),
]
