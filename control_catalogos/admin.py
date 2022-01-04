from django.contrib import admin
from .models import Paises, Dependencias, Departamentos, Personas

# Register your models here.
admin.site.register(Paises)
admin.site.register(Dependencias)
admin.site.register(Departamentos)
admin.site.register(Personas)