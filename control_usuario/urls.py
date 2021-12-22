from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Bienvenida_view, name="Bienvenida_view"),
    path('login/', views.login_view, name="login_view"),
    path('home/', views.Home_view, name="Home_view"),
]