from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.get_all_tasks, name="get_all_tasks"),
    path('create', views.create_task, name="create_task"),
    path('delete/<uuid:id>', views.delete_task, name="delete_task"),
    path('update/<uuid:id>', views.update_task, name="update_task"),
    path('<str:project_id>', views.get_task, name="get_task"),
]