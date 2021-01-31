from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import sparkTokenSerializer
from .models import sparkToken
from django.utils import timezone
from uuid import uuid4
from datetime import datetime, timedelta
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Generate': '/generate/',
        'Add': '/add/',
        'Delete': '/delete/',
        'Extend': '/extend/',
        'ALL Tokens': '/tokenList/',
        'Assign': '/assign/',
        'Unblock': '/unblock/',

    }
    return Response(api_urls)

@api_view(['GET'])
def tokenList(request):
    timeout()
    tokens = sparkToken.objects.all()
    serializer = sparkTokenSerializer(tokens,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generate(request):
    key_expires = timezone.now() + timedelta(seconds=60)
    token = sparkToken(token=generateNewToken(),valid_till=key_expires,locked=False)
    token.save()
    serializer = sparkTokenSerializer(token,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def tokenAdd(request):
    serializer = sparkTokenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def details(request, pk):
    tokens = sparkToken.objects.get(id=pk)
    serializer = sparkTokenSerializer(tokens,many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, pk):
    tokens = sparkToken.objects.get(id=pk)
    tokens.delete()
    return Response('Token deleted')

def timeout():
    key_expires = timezone.now() - timedelta(seconds=60)
    tokens = sparkToken.objects.filter(valid_till__lte=key_expires).update(locked=False)
    key_expires = timezone.now() - timedelta(minutes=5)
    dealt = sparkToken.objects.filter(valid_till__lte=key_expires).delete()

    

@api_view(['GET'])
def extend(request, pk):
    tokens = sparkToken.objects.get(id=pk)
    if tokens.locked == True and tokens.valid_till > timezone.now():
        tokens.valid_till = timezone.now() + timedelta(seconds=60)
        tokens.locked = True
    else:
        tokens.locked = False    
    tokens.save()
    serializer = sparkTokenSerializer(instance= tokens,many=False)
    return Response(serializer.data)

def generateNewToken():
    rand_token = uuid4()
    return rand_token

@api_view(['GET'])
def assign(request):
    tokens = sparkToken.objects.filter(locked=False).first()
    if tokens is not None:
        tokens.valid_till = timezone.now() + timedelta(minutes=60)
        tokens.locked = True
        tokens.save()
        serializer = sparkTokenSerializer(instance= tokens,many=False)
        return Response(serializer.data)
    else:
        return Response('No valid token available',status=404)
        
    
    
    

@api_view(['GET'])
def unblock(request, pk):
    tokens = sparkToken.objects.get(id=pk)
    if tokens.locked == True:
        tokens.locked = False
    tokens.save()
    serializer = sparkTokenSerializer(instance= tokens,many=False)
    return Response(serializer.data)
