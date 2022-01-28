from django.urls import path
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('eventos/', views.eventos_view, name="eventos_view"), #Url para acceder a la vista eventos_view
    path('eventos_altas/', views.eventos_altas_view, name="eventos_altas_view"), #Url para acceder a la vista eventos_altas_view
]