from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Bienvenida_view, name="Bienvenida_view"),
]