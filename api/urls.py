from django.urls import path
from . import views

from .models import Service

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/services', views.getServices, name="services"),
    
]