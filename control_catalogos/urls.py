from django.urls import path
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('administracion/', views.administracion_view, name="administracion_view"), #Url para acceder a la vista administracion_view
    path('seleccion_continente/', views.seleccion_continente_view, name="seleccion_continente_view"), #Url para acceder a la vista seleccion_continente_view
    path('cat_paises/', views.cat_paises_view, name="cat_paises_view"), #Url para acceder a la vista cat_paises_view
    path('cat_dependencias/', views.cat_depenencias_view, name="cat_depenencias_view"), #Url para acceder a la vista cat_depenencias_view
    path('cat_departamentos/', views.cat_departamentos_view, name="cat_departamentos_view"), #Url para acceder a la vista cat_departamentos_view
    path('cat_personas/', views.cat_personas_view, name="cat_personas_view"), #Url para acceder a la vista cat_personas_view
]

# <int:model_id>