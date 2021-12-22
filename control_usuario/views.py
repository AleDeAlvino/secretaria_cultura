from django.shortcuts import render

# Create your views here.
def Bienvenida_view(request):
    return render(request, 'Bienvenida.html', {'var': 'bienvenida'})

def Home_view(request):
    return render(request, 'Home.html')

def login_view(request):
    return render(request, 'login.html', {'var': 'login'})