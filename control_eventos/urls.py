from django.urls import path
from .import views

# Urls para acceder a las vistas pertenecientes a control usuarios
urlpatterns = [
    path('eventos/', views.eventos_view, name="eventos_view"), #Url para acceder a la vista eventos_view
]