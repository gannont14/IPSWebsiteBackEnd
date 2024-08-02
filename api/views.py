from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.decorators import api_view, parser_classes

import json

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Service, Photo, AboutMainContent
from .serializers import ServiceSerializer, PhotoSerializer, AboutMainContentserializer


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



@api_view(['GET', 'POST', 'PUT', 'PATCH'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def getAboutMainContent(request):
    if request.method == 'GET':
        content = AboutMainContent.objects.all()
        serializer = AboutMainContentserializer(content, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
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







# login view for auth
    
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'failure'}, status=403)
    return JsonResponse({'status': 'failure'}, status=405)


# view to logout
@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail', 'message': 'Invalid request'}, status=400)

# checking auth
def check_authentication(request):
    if request.user.is_authenticated:
        return JsonResponse({'status': 'authenticated'})
    return JsonResponse({'status': 'not_authenticated'})