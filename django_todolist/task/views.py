from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.db import IntegrityError, OperationalError
import json
from project.models import Project
from task.models import Task

@csrf_exempt
@require_POST
def create_task(request):
    try:
        data = json.loads(request.body)
        
        # Verifica che il progetto esista
        project = Project.objects.get(id=data['project_id'])
        
        task = Task.objects.create(
            title=data['title'],
            project=project
        )
        
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'is_complete': task.is_complete,
            'project_id': task.project.id
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    
    except KeyError as e:
        return JsonResponse({'error': f'Campo mancante: {e}'}, status=400)
    
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Progetto non trovato'}, status=404)
    
    except IntegrityError:
        return JsonResponse({'error': 'Task già esistente'}, status=409)

@require_GET
def get_task(request, project_id):
    try:
        # 1. Usa filter() invece di get() - un progetto può avere più task
        # 2. Usa values() per serializzare
        tasks = list(Task.objects.filter(project_id=project_id).values())
        
        return JsonResponse(tasks, safe=False, status=200)
    
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'message': 'Task eliminato con successo'}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task non trovato'}, status=404)
    except OperationalError:
        return JsonResponse({'error': 'Errore del database'}, status=503)

@csrf_exempt
@require_http_methods(["PATCH"])
def update_task(request, id):
    try:
        data = json.loads(request.body)
        task = Task.objects.get(id=id)
        
        if 'title' in data:
            task.title = data['title']
        if 'is_complete' in data:
            task.is_complete = data['is_complete']
            
        task.save()
        
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'is_complete': task.is_complete,
            'project_id': task.project.id
        }, status=200)

    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task non trovato'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)
    except IntegrityError:
        return JsonResponse({'error': 'Titolo già esistente'}, status=409)
    except OperationalError:
        return JsonResponse({'error': 'Errore del database'}, status=503)

@require_GET
def get_all_tasks(request):
    try:
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False, status=200)
    except OperationalError:
        return JsonResponse({'error': 'Database non disponibile'}, status=503)