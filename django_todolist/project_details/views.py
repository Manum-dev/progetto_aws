from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from django.http import JsonResponse
from project_details.models import ProjectDetails

@csrf_exempt
@require_http_methods(['PATCH'])
def update_details_project(request, id):

    try:
        data = json.loads(request.body)
        print('data', data)
        projects_details = ProjectDetails.objects.get(id=id)
        
        
        if data["notes"]:
            projects_details.notes = data['notes']
        
        projects_details.save()
        
        return JsonResponse({
            'id': projects_details.id,
            'notes': projects_details.notes
        }, status=200)
    
    except ProjectDetails.DoesNotExist:
        return JsonResponse({'error': 'Dettaglio progetto non trovato'}, status=404)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON non valido'}, status=400)