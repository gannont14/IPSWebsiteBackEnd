from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt import views as jwt_views



from . import views

from .models import Service

urlpatterns = [

    path('api/services/', views.getServices, name="services"),
    path('api/services/<str:serviceId>/', views.getServiceById, name="get_service_by_id"),                            
    path('api/services/modify', views.updateServices, name="updateServices"),

    path('api/photos', views.getPhotos, name="photos"),
    path('api/photos/modify', views.updatePhotos, name="updatePhotos"),

    path('api/aboutMainContent', views.getAboutMainContent, name="aboutMainContent"),
    path('api/aboutMainContent/modify', views.updateAboutMainContent, name="updateMainContent"),
    path('api/aboutMainContent/<int:itemId>/modify', views.updateAboutMainContent, name="updateMainContent"),
    
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
