from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
# from .forms import PaisForm
from .models import Paises, Dependencias, Departamentos

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
            if conti != 'Selecciona un continente': #Si es diferente de la opción default procede
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
                        # continente_env = valor[valor.find('-')+1:]
                        if Paises.objects.filter(pais=pais_env).exists(): #Verificamos si existe el país que se mandó
                            if request.POST['btn_env'] == 'Actualizar': #Si la opción que eligio fue Actualizar procede
                                pais_editar = Paises.objects.get(pais=pais_env)
                                if pais_env != request.POST['pais'] or pais_editar.continente !=request.POST['select_Continente']: #Verificamos que realmente hubo cambios
                                    pais_editar.pais = request.POST['pais'] #Le damos el nuevo valor de país
                                    pais_editar.continente = request.POST['select_Continente'] #Le damos el nuevo valor de continente
                                    pais_editar.save() #Se guardan los cambios
                                    messages.success(request, 'País actualizado')
                                else:
                                    messages.error(request, 'No ha habido ningún cambio')
                            elif request.POST['btn_env'] == 'Eliminar': #Si la opción que eligio fue eliminar procede
                                pais_borrar = get_object_or_404(Paises,pais=pais_env) #Traemos el objeto a eliminar
                                pais_borrar.delete(); #Se elimina
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


def cat_depenencias_view(request):
    #Vista para agregar, editar y eliminar dependencias del catalogo dependencias
    paises = Paises.objects.all().order_by('pais') #Traemos todos los paises de la bd para mostrarlos en el select
    dependencias = Dependencias.objects.all().order_by('dependencia') #Traemos todos las dependencias de la bd para mostrarlos en el select
    if request.method == 'POST': #Si el formulario a sido mandado por POST empieza el proceso
        if request.POST['dependencia'] != '' : #Nos aseguramos que el campo dependencia no esté vacio
            pais_sel = request.POST['select_Pais'] #Traemos el valor de país
            if pais_sel != 'Selecciona un país': #Si es diferente de la opción default procede
                if Paises.objects.filter(pais=pais_sel).exists(): #Nos aseguramos que solo haya escogido alguna opción del select
                    if request.POST['option-pert'] == 'True' or request.POST['option-pert'] == 'False':
                        if request.POST['btn_env'] == 'Agregar': #Si la opción que eligio fue agregar procede
                            try:
                                pais = Paises.objects.get(pais=pais_sel)
                                dependencia, created = Dependencias.objects.get_or_create(pais=pais, dependencia=request.POST['dependencia'], pertenencia=request.POST['option-pert']) #Comando para saber si existe o no el objeto, si no existe lo crea
                                if created:
                                    dependencia.save() #Se guarda el nuevo objeto
                                    messages.success(request, 'Se agregó la dependencia correctamente')
                                else:
                                    messages.error(request, 'Ya existe la dependencia ' + request.POST['dependencia'])
                            except IntegrityError:
                                messages.error(request, 'Ya existe la dependencia')
                        else:
                            valor = request.POST['select_Dependencia_cat']
                            dependencia = valor[0:valor.find('-')] #Extraemos el valor enviado dejando solamente la dependencia
                            pais = valor[valor.find('-')+1:valor.find('+')]
                            pertenencia = valor[valor.find('+')+1:]
                            print(pertenencia);
                            if Dependencias.objects.filter(dependencia=dependencia).exists():
                                if request.POST['btn_env'] == 'Actualizar': #Si la opción que eligio fue Actualizar procede
                                    if Paises.objects.filter(pais=pais).exists(): #Verificamos si existe el país que se mandó
                                        if pertenencia == 'True' or pertenencia == 'False':
                                            print('Hola')
                                            if request.POST['dependencia'] != dependencia or pais_sel != pais or request.POST['option-pert'] != pertenencia:
                                                dependecia_editar = Dependencias.objects.get(dependencia=dependencia)
                                                dependecia_editar.dependencia = request.POST['dependencia']
                                                pais_recuperado = Paises.objects.get(pais=pais_sel)
                                                dependecia_editar.pais = pais_recuperado
                                                dependecia_editar.pertenencia = request.POST['option-pert']
                                                dependecia_editar.save()
                                                messages.success(request, 'Dependencia actualizada')
                                            else:
                                                messages.error(request, 'No ha habido ningún cambio')
                                        else:
                                            messages.error(request, 'Solo puedes escoger Si o No')
                                    else:
                                        messages.error(request, 'Este país no existe')
                                elif request.POST['btn_env'] == 'Eliminar': #Si la opción que eligio fue eliminar procede
                                    print('Hola2')
                                    dependencia_borrar = get_object_or_404(Dependencias,dependencia=dependencia) #Traemos el objeto a eliminar
                                    dependencia_borrar.delete()
                                    messages.success(request, 'Dependencia eliminada')
                                else:
                                    messages.error(request, 'No existe esa opción')
                            else:
                                messages.error(request, 'La dependencia no existe')
                    else:
                        messages.error(request, 'Solo puede seleccionar Si o No')
                else:
                    messages.error(request, 'No existe ese pís')
            else:
                messages.error(request, 'No has seleccionado ningun país')
        else:
            messages.error(request, 'El campo Dependencia está vacío')
    return render(request, 'catalogo_dependencias.html', {'paises':paises, 'dependencias':dependencias})


def cat_departamentos_view(request):
    #Vista para agregar, editar y eliminar departamentos del catalogo departamentos
    dependencias = Dependencias.objects.all().order_by('dependencia') #Traemos todos las dependencias de la bd para mostrarlos en el select
    departamentos = Departamentos.objects.all().order_by('departamento') #Traemos todos las departamentos de la bd para mostrarlos en el select
    if request.method == 'POST': #Si el formulario a sido mandado por POST empieza el proceso
        if request.POST['departamento'] != '' : #Nos aseguramos que el campo departamento no esté vacio
            dependencia_sel = request.POST['select_Dependencia'] #Traemos el valor de dependencia
            if dependencia_sel != 'Selecciona una Dependencia': #Si es diferente de la opción default procede
                if Dependencias.objects.filter(dependencia=dependencia_sel).exists(): #Nos aseguramos que solo haya escogido alguna opción del select
                    if request.POST['btn_env'] == 'Agregar': #Si la opción que eligio fue agregar procede
                        try:
                            dependencia = Dependencias.objects.get(dependencia=dependencia_sel)
                            departamento, created = Departamentos.objects.get_or_create(dependencia=dependencia, departamento=request.POST['departamento']) #Comando para saber si existe o no el objeto, si no existe lo crea
                            if created:
                                departamento.save() #Se guarda el nuevo objeto
                                messages.success(request, 'Se agregó el departamento correctamente')
                            else:
                                messages.error(request, 'Ya existe el departamento ' + request.POST['departamento'])
                        except IntegrityError:
                            messages.error(request, 'Ya existe el departamento')
                    else:
                        valor = request.POST['select_departamento_cat']
                        departamento = valor[0:valor.find('-')] #Extraemos el valor enviado dejando solamente el departamento
                        if Departamentos.objects.filter(departamento=departamento).exists():
                            if request.POST['btn_env'] == 'Actualizar': #Si la opción que eligio fue Actualizar procede
                                departamento_editar = Departamentos.objects.get(departamento=departamento)
                                if request.POST['departamento'] != departamento or dependencia_sel != departamento_editar.dependencia.dependencia:
                                    dependencia_rec = Dependencias.objects.get(dependencia=dependencia_sel)
                                    departamento_editar.dependencia = dependencia_rec
                                    departamento_editar.departamento = request.POST['departamento']
                                    departamento_editar.save()
                                    messages.success(request, 'Dependencia actualizada')
                                else:
                                    messages.error(request, 'No ha habido ningún cambio')
                                
                            elif request.POST['btn_env'] == 'Eliminar': #Si la opción que eligio fue eliminar procede
                                print('Hola2')
                                # dependencia_borrar = get_object_or_404(Dependencias,dependencia=dependencia) #Traemos el objeto a eliminar
                                # dependencia_borrar.delete()
                                messages.success(request, 'Dependencia eliminada')
                            else:
                                messages.error(request, 'No existe esa opción')
                        else:
                            messages.error(request, 'El departamento no existe')
                else:
                    messages.error(request, 'No existe esa dependencia')
            else:
                messages.error(request, 'No has seleccionado ninguna Dependencia')
        else:
            messages.error(request, 'El campo Departamento está vacío')
    return render(request, 'catalogo_departamentos.html', {'dependencias':dependencias, 'departamentos':departamentos})