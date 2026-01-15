from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

title_data ={
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  }
  
  

def comment (request):
    return JsonResponse(title_data)