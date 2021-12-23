from django.shortcuts import render

# Create your views here.
def Bienvenida_view(request):
    # Esta vista solamente nos mostrara la pantalla de bienvenida y envia el parametro 'bienvenida' para que se muestre el boton de inicio de sesión
    return render(request, 'Bienvenida.html', {'var': 'bienvenida'})

def Home_view(request):
    # Esta vista nos mostrara la primera pantalla del home una vez iniciada la sesión
    return render(request, 'Home.html')

def login_view(request):
    # Esta vista se encarga de procesar los datos enviados por el formulario para saber si es valido o no
    return render(request, 'login.html', {'var': 'login'})