from django.urls import path, include
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('', views.Bienvenida_view, name="Bienvenida_view"), #Url para acceder a la vista Bienvenida_view
    path('login/', views.login_view, name="login_view"), #Url para acceder a la vista login_view
    path('home/', views.Home_view, name="Home_view"), #Url para acceder a la vista Home_view
]