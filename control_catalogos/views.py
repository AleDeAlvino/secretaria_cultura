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
    #Vista para agregar, editar y eliminar paises del catalogo de paises
    paises = Paises.objects.all().order_by('pais') #Traemos todos los paises de la bd para mostrarlos en el select
    if request.method == 'POST': #Si el formulario a sido mandado por POST empieza el proceso
        if request.POST['pais'] != '' : #Nos aseguramos que el campo país no esté vacio
            conti = request.POST['select_Continente'] #Traemos el valor de continente
            if conti != 'Selecciona un continente': #Si es diferente de la opción defaul procede
                if conti == 'Asia' or conti == 'América' or conti == 'África' or conti == 'Antartida' or conti == 'Europa' or conti == 'Oceanía': #Nos aseguramos que solo haya escogido alguna opción del select
                    if request.POST['btn_env'] == 'Agregar': #Si la opción que eligio fue agregar procede
                        try:
                            pais, created = Paises.objects.get_or_create(pais=request.POST['pais'], continente=request.POST['select_Continente']) #Comando para saber si existe o no el objeto, si no existe lo crea
                            if created:
                                pais.save() #Se guarda el nuevo objeto
                                messages.success(request, 'Se agregó el país correctamente')
                            else:
                                messages.error(request, 'Ya existe el país ' + request.POST['pais'])
                        except IntegrityError:
                            messages.error(request, 'Ya existe el país ')
                    else:
                        valor = request.POST['select_Pais_cat']
                        pais_env = valor[0:valor.find('-')] #Extraemos el valor enviado dejando solamente el país
                        continente_env = valor[valor.find('-')+1:]
                        if Paises.objects.filter(pais=pais_env).exists(): #Verificamos si existe el país que se mandó
                            if continente_env == 'Asia' or continente_env == 'América' or continente_env == 'África' or continente_env == 'Antartida' or continente_env == 'Europa' or continente_env == 'Oceanía':
                                if request.POST['btn_env'] == 'Actualizar': #Si la opción que eligio fue Actualizar procede
                                    if pais_env != request.POST['pais'] or continente_env !=request.POST['select_Continente']: #Verificamos que realmente hubo cambios
                                        pais_editar = Paises.objects.get(pais=pais_env)
                                        pais_editar.pais = request.POST['pais'] #Le damos el nuevo valor de país
                                        pais_editar.continente = request.POST['select_Continente'] #Le damos el nuevo valor de continente
                                        pais_editar.save() #Se guardan los cambios
                                        messages.success(request, 'País actualizado')
                                    else:
                                        messages.error(request, 'No ha habido ningun cambio')
                                elif request.POST['btn_env'] == 'Eliminar': #Si la opción que eligio fue eliminar procede
                                    pais_borrar = get_object_or_404(Paises,pais=pais_env) #Traemos el objeto a eliminar
                                    pais_borrar.delete(); #Se elimina
                                    messages.success(request, 'País Eliminado')
                                else:
                                    messages.error(request, 'No existe esa opcion')
                            else:
                                messages.error(request, 'No existe ese continente')
                        else:
                            messages.error(request, 'Este país no existe')
                else:
                    messages.error(request, 'No existe ese continente')
            else:
                messages.error(request, 'No has seleccionado ningun continente')
        else:
            messages.error(request, 'El campo país está vacío')
    return render(request, 'catalogo_paises.html', {'paises':paises})