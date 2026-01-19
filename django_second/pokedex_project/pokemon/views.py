from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Pokemon
import json

# Create your views here.
def pokemon_list(request):
    if not Pokemon.objects.exists():
        # Se è vuoto, crea dei Pokemon di prova
        Pokemon.objects.create(name="Pikachu", type="Elettro", levels=15, descriptions="Giallo")
        Pokemon.objects.create(name="Bulbasaur", type="Erba", levels=10, descriptions="Verde")
        print("Database popolato con successo!")
    pokemons = Pokemon.objects.all().values()
    return JsonResponse(list(pokemons), safe=False)

def pokemon_add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_pokemon = Pokemon.objects.create(
                name=data.get('name'),
                type=data.get('type'),
                levels=data.get('levels', 1),
                descriptions=data.get('description', '')
            )
            return JsonResponse({"message": "Creato!", "id": new_pokemon.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Metodo non consentito"}, status=405)

def pokemon_delete(request, id):
    if request.method == 'DELETE'or request.method == 'POST': 
        pokemon = get_object_or_404(Pokemon, id=id)
        pokemon.delete()
        return JsonResponse({"message": f"Pokemon {id} eliminato!"})
    return JsonResponse({"error": "Metodo non consentito"}, status=405)