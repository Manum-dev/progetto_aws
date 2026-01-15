from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

title_data ={
    "userId": 1,
    "id": 1,
    "title": "quidem molestiae enim"
  }
def index(request):
    return HttpResponse("Hello, world. You're at the albums index.")


def album(request):
    return JsonResponse(title_data)