from django.urls import path, include
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('administracion/', views.administracion_view, name="administracion_view"), #Url para acceder a la vista administracion_view
    path('cat_paises/', views.cat_paises_view, name="cat_paises_view"), #Url para acceder a la vista cat_paises_view
]