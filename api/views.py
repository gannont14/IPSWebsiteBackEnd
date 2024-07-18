from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, parser_classes


from .models import Service, Photo
from .serializers import ServiceSerializer, PhotoSerializer


# Create your views here.

# testing endpoint, not used for anything
@api_view(['GET'])
def getRoutes(request):
    return Response('TestApi')

# currently just a get and post available
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
# used for uploading images, as well as parsing JSON request to put and patch requests
@parser_classes([MultiPartParser, FormParser, JSONParser])
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
    elif request.method in  ['PUT', 'PATCH']:
        itemId = request.data.get('id')
        try:
            item = Service.objects.get(id=itemId)
        except Service.DoesNotExist:
             return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ServiceSerializer(item, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# View to collect all of the photos for the photo gallery
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def getPhotos(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PhotoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method in ['PUT', 'PATCH']:
        itemId = request.data.get('id')
        if not itemId:
            return Response({'error': 'Item id not present'}, status=status.HTTP_404_NOT_FOUND)
        try:
            item = Photo.objects.get(id=itemId)
        except Photo.DoesNotExist:
             return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PhotoSerializer(item, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
