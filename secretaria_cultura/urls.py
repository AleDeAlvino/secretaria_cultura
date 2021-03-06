"""secretaria_cultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #Esta ruta nos va a permitir acceder al administrador de Django
    path('', include('control_usuario.urls')), #Conección con las url de la aplicación control_usuario
    path('', include('control_catalogos.urls')), #Conección con las url de la aplicación control_catalogos
    path('', include('control_eventos.urls')), #Conección con las url de la aplicación control_eventos
]
