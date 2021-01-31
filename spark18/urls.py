"""spark18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sparkToken.views import apiOverview, tokenList, tokenAdd
from sparkToken.views import generate, assign, unblock
from sparkToken.views import extend, delete, details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',apiOverview, name='apiOverview'),
    path('tokenList/',tokenList, name='tokenList'),
    path('add/',tokenAdd, name='tokenAdd'),
    path('generate/',generate, name='generate'),
    path('extend/<str:pk>/',extend, name='extend'),
    path('delete/<str:pk>/',delete, name='delete'),
    path('details/<str:pk>/',details, name='details'),
    path('assign/',assign, name='assign'),
    path('unblock/<str:pk>/',unblock, name='unblock'),
]
