from django.db import models

# Create your models here.

#Modelo de paises donde especificamos los campos y sus CONSTRAINT
class Paises(models.Model):
    pais = models.CharField(max_length = 50, unique=True)
    continente = models.CharField(max_length = 10)
    def __str__(self):
         return "{}".format(self.pais) #manera en que visualizamos el objeto en el admin

class Dependencias(models.Model):
    pais = models.ForeignKey(Paises, on_delete=models.CASCADE)
    dependencia = models.CharField(max_length = 50, unique=True)
    pertenencia = models.BooleanField(default=False)
    def __str__(self):
         return "{}".format(self.dependencia)

class Departamentos(models.Model):
    dependencia = models.ForeignKey(Dependencias, on_delete=models.CASCADE)
    departamento = models.CharField(max_length = 80, unique=True)
    def __str__(self):
         return "{}".format(self.departamento)