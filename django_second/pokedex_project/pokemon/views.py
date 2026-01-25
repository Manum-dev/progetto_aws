from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Pokemon
from django.views.decorators.http import require_POST

# Create your views here.
def pokemon_list(request):
    if not Pokemon.objects.exists():
        # Se è vuoto, crea dei Pokemon di prova
        Pokemon.objects.create(name="Pikachu", type="Elettro", levels=15, descriptions="Giallo")
        Pokemon.objects.create(name="Bulbasaur", type="Erba", levels=10, descriptions="Verde")
        print("Database popolato con successo!")
    pokemons = Pokemon.objects.all().values()
    return JsonResponse(list(pokemons), safe=False)

def add_pokemon(request):
    pokemon = Pokemon.objects.create(name="Bulbasaur", pokedex_id=1)
    return JsonResponse({'id': pokemon.id, 'name': pokemon.name, 'pokedex_id': pokemon.pokedex_id})

def pokemon_delete(request, id):
    if request.method == 'DELETE'or request.method == 'POST': 
        pokemon = get_object_or_404(Pokemon, id=id)
        pokemon.delete()
        return JsonResponse({"message": f"Pokemon {id} eliminato!"})
    return JsonResponse({"error": "Metodo non consentito"}, status=405)