from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import sparkTokenSerializer
from .models import sparkToken
from django.utils import timezone
from uuid import uuid4
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Generate': '/generate/',
        'Add': '/add/',
        'Delete': '/delete/',
        'Extend': '/extend/',
        'ALL Tokens': '/tokenList/',

    }
    return Response(api_urls)

@api_view(['GET'])
def tokenList(request):
    tokens = sparkToken.objects.all()
    serializer = sparkTokenSerializer(tokens,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generate(request):
    key_expires = timezone.now() + datetime.timedelta(seconds=60)
    token = sparkToken(token=generateNewToken,valid_till=key_expires,locked=False)
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

@api_view(['POST'])
def extend(request, pk):
    tokens = sparkToken.objects.get(id=pk)
    tokens.valid_till = timezone.now() + datetime.timedelta(days=2)
    serializer = sparkTokenSerializer(instance= tokens,data=request.data)
    return Response(serializer.data)

def generateNewToken():
    rand_token = uuid4()
    return rand_token

