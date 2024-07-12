from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Service
from .serializers import ServiceSerializer


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('TestApi')


@api_view(['GET'])
def getServices(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)