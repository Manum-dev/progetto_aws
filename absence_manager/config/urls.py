"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py
# config/urls.py
from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from absences.views import AbsenceListCreateView


# Una piccola home di cortesia per non avere il 404
def home_view(request):
    return JsonResponse({
        "status": "online",
        "project": "Absence Manager API",
        "endpoints": ["/register/", "/login/", "/token/refresh/"]
    })

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    
    # Rotte ultra-pulite
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('absences/', AbsenceListCreateView.as_view(), name='absence-list'),
]
