from django.shortcuts import render, redirect, get_object_or_404
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
    paises = Paises.objects.all().order_by('pais')
    if request.method == 'POST':
        if request.POST['pais'] != '' :
            conti = request.POST['select_Continente']
            if conti != 'Selecciona un continente':
                if conti == 'Asia' or conti == 'América' or conti == 'África' or conti == 'Antartida' or conti == 'Europa' or conti == 'Oceanía':
                    if request.POST['btn_env'] == 'Agregar':
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
                        valor = request.POST['select_Pais_cat']
                        pais_env = valor[0:valor.find('-')]
                        if Paises.objects.filter(pais=pais_env).exists():
                            if request.POST['btn_env'] == 'Editar':
                                if pais_env != request.POST['pais']:
                                    pais_editar = Paises.objects.get(pais=pais_env)
                                    pais_editar.pais = request.POST['pais']
                                    pais_editar.continente = request.POST['select_Continente']
                                    pais_editar.save()
                                    messages.success(request, 'País actualizado')
                                else:
                                    messages.error(request, 'No ha habido ningun cambio')
                            elif request.POST['btn_env'] == 'Eliminar':
                                pais_borrar = get_object_or_404(Paises,pais=pais_env)
                                pais_borrar.delete();
                                messages.success(request, 'País Eliminado')
                            else:
                                messages.error(request, 'No existe esa opcion')
                        else:
                            messages.error(request, 'Este país no existe')
                else:
                    messages.error(request, 'No existe ese continente')
            else:
                messages.error(request, 'No has seleccionado ningun continente')
        else:
            messages.error(request, 'El campo país está vacío')
    return render(request, 'catalogo_paises.html', {'paises':paises})