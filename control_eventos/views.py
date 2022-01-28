
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..control_catalogos.models import Paises, Dependencias, Departamentos, Personas

def eventos_view(request):
    #Vista para mostrar todos las opciones de eventos
    return render(request, 'eventos.html')