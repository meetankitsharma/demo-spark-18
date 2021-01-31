from django.shortcuts import render
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

def tokenList(request):
    tokens = sparkToken.Object.all()
    serializer = sparkTokenSerializer(tokens,many=True)
    return Response()
