from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.pokemon_list, name="pokemon_list"),
    path('', views.pokemon_add, name='pokemon_add'),
    path("delete/", views.pokemon_delete, name= 'pokemon_delete')
]