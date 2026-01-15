from django.urls import path

from . import views


urlpatterns = [
    path("", views.album, name="album"),
    path("messaggio/", views.index, name="index"),
]
