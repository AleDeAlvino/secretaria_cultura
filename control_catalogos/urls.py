from django.urls import path, include
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('administracion/', views.administracion_view, name="administracion_view"), #Url para acceder a la vista administracion_view
]