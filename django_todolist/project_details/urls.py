from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_all_details, name="get_all_details"),
    path('<str:id>', views.update_details_project, name="update_details_project"),
]