from django.shortcuts import render

# Create your views here.
def administracion_view(request):
    #
    return render(request, 'administracion.html')

def cat_paises_view(request):
    #
    return render(request, 'catalogo_paises.html')