from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import sparkTokenSerializer
from .models import sparkToken
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

@api_view(['POST'])
def tokenAdd(request):
    serializer = sparkTokenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)