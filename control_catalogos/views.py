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
    paises = Paises.objects.all()
    if request.method == 'POST':
        print(request.POST['pais'])
        if request.POST['btn_env'] == 'Agregar':
            print('fue agregar')
            if request.POST['pais'] != '' :
                conti = request.POST['select_Continente']
                if conti != 'Selecciona un continente':
                    if conti == 'Asia' or conti == 'América' or conti == 'África' or conti == 'Antartida' or conti == 'Europa' or conti == 'Oceanía':
                        try:
                            pais, created = Paises.objects.get_or_create(pais=request.POST['pais'], continente=request.POST['select_Continente'])
                            if created:
                                pais.save()
                                messages.success(request, 'Se agregó el país correctamente')
                            else:
                                messages.error(request, 'Ya existe el país ' + request.POST['pais'])
                        except IntegrityError:
                            messages.error(request, 'Ya existe el país ')
                    else:
                        messages.error(request, 'No existe ese continente')
                else:
                    messages.error(request, 'No has seleccionado ningun continente')
            else:
                messages.error(request, 'El campo país está vacío')
        else:
            print('fue editar')
            if request.POST['pais'] != '' :
                pais_editar = request.POST['select_Pais_cat']
            else:
                messages.error(request, 'El campo país está vacío')
            # messages.success(request, 'fue editar')
    return render(request, 'catalogo_paises.html', {'paises':paises})