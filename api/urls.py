from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views



from . import views

from .models import Service

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('api/services', views.getServices, name="services"),
    path('api/photos', views.getPhotos, name="photos"),
    path('api/aboutMainContent', views.getAboutMainContent, name="aboutMainContent"),
    path('api/check_authentication', views.check_authentication, name="check_authentication"),
    path('api/login',  views.login_view, name='login_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)