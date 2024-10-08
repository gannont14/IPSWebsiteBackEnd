from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


from .models import Service, Photo, AboutMainContent
from .serializers import ServiceSerializer, PhotoSerializer, AboutMainContentserializer


# Create your views here.

@api_view(['GET'])
# available to all users, does not require token to fetch information
@parser_classes([MultiPartParser, FormParser, JSONParser])
def getServices(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def getServiceById(request, serviceId):
    if request.method == 'GET':
        try:
            service = Service.objects.get(serviceId=serviceId)
            serializer = ServiceSerializer(service)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def getPhotos(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getAboutMainContent(request):
    if request.method == 'GET':
        content = AboutMainContent.objects.all()
        serializer = AboutMainContentserializer(content, many=True)
        return Response(serializer.data)

# Requires user to be authorized to update information
@api_view(['PATCH', 'PUT', 'POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def updateServices(request):
    if request.method == 'POST':
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
@api_view(['POST', 'PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def updatePhotos(request):
    if request.method == 'POST':
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



@api_view(['POST', 'PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
@permission_classes([IsAuthenticated])
def updateAboutMainContent(request):
    if request.method == 'POST':
        serializer = AboutMainContentserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        itemId = request.data.get('id')
        if not itemId:
            return Response({'error': 'Item id not present'}, status=status.HTTP_404_NOT_FOUND)
        try:
            item = AboutMainContent.object.get(id=itemId)
        except AboutMainContent.DoesNotExist:
            return Response({'error': 'Item id not present'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AboutMainContentserializer(item, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)

