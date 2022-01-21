
"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
# from turtle import home
from django.contrib import admin
from django.urls import path
# from enroll.models import addtech,addgit
from enroll import views
from django.http import HttpResponse

urlpatterns = [
    path('index/',views.index,name="index"),
    path('update/',views.update),
    path('addtech/',views.adtech,name="addtech"),
    path('home/',views.home),
    path('tech/',views.tech,name="tech"),
    path('git/',views.git,name='git'),
    path('addgit/',views.addgit,name="adgit"),
    path('styling/',views.style, name="style"),
    path('update/',views.update_project,name="update")
    
    
]
