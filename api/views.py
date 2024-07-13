from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, parser_classes


from .models import Service
from .serializers import ServiceSerializer


# Create your views here.

# testing endpoint, not used for anything
@api_view(['GET'])
def getRoutes(request):
    return Response('TestApi')

# currently just a get and post available
@api_view(['GET', 'POST'])
# used for uploading images
@parser_classes([MultiPartParser, FormParser])
def getServices(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ServiceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)