from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
# from .forms import PaisForm
from .models import Paises

# Create your views here.
def administracion_view(request):
    #Vista para mostrar todos los catalogos
    return render(request, 'administracion.html')

def cat_paises_view(request):
    #Vista para editar el catalogo de paises
    if request.method == 'POST':
        print(request.POST['pais'])
        if request.POST['pais'] != '' :
            try:
                pais, created = Paises.objects.get_or_create(pais=request.POST['pais'])
                if created:
                    pais.save()
                    messages.success(request, 'Se agregó el país correctamente')
                else:
                    messages.error(request, 'Ya existe el país ' + request.POST['pais'])
            except IntegrityError:
                messages.error(request, 'Ya existe el país ')
        else:
            messages.error(request, 'El campo país está vacío')
    return render(request, 'catalogo_paises.html')