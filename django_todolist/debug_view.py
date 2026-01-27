
import os
import django
import json
from django.test import RequestFactory
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todolist.settings')
django.setup()

from task.views import create_task
from project.models import Project

def test_view():
    factory = RequestFactory()
    
    print("--- Test 1: Empty Body ---")
    request = factory.post('/task/create', content_type='application/json', data='')
    response = create_task(request)
    print(f"Status: {response.status_code}")
    print(f"Content: {response.content.decode()}")

    print("\n--- Test 2: Invalid JSON ---")
    request = factory.post('/task/create', data='params=1', content_type='application/json')
    response = create_task(request)
    print(f"Status: {response.status_code}")
    print(f"Content: {response.content.decode()}")

    print("\n--- Test 3: Missing Keys ---")
    request = factory.post('/task/create', data=json.dumps({'title': 'Foo'}), content_type='application/json')
    response = create_task(request)
    print(f"Status: {response.status_code}")
    print(f"Content: {response.content.decode()}")

if __name__ == "__main__":
    test_view()
