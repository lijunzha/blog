"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from sys import path

from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path(r'', views.home),
    path(r'post/home/', views.home),
    path(r'post/article/', views.article),
    path(r'post/editor/', views.editor),
    path(r'post/search/', views.search),
    path(r'post/comment/', views.comment),
]
