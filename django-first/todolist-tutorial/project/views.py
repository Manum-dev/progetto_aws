from django.shortcuts import render
from models import Project
from django.http import JsonResponse
from .models import Project

# Create your views here.

from django.http import HttpResponse, JsonResponse

def index(request):
    project = Project.objects.all().values()
    return JsonResponse("Hello, world. You're at the projects index.")

