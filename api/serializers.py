from rest_framework.serializers import ModelSerializer
from .models import Service
from .models import Photo
from .models import AboutMainContent


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service 
        fields = '__all__'


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo 
        fields = '__all__'

class AboutMainContentserializer(ModelSerializer):
    class Meta:
        model = AboutMainContent
        fields = '__all__'