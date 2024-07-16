from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from .models import Service

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/services', views.getServices, name="services"),
    path('api/photos', views.getPhotos, name="photos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)