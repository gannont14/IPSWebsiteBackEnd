from rest_framework.serializers import ModelSerializer
from .models import Service
from .models import Photo


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service 
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo 
        fields = '__all__'
