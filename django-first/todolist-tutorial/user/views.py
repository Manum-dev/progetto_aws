from django.shortcuts import render
from .data import user_list

# Create your views here.

from django.http import JsonResponse

def users(request):
    return JsonResponse (user_list, safe=False)


