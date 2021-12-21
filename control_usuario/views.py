from django.shortcuts import render

# Create your views here.
def Bienvenida_view(request):
    return render(request, 'Bienvenida.html')