from django.db import models

# Create your models here.

#Modelo de paises donde especificamos los campos y sus CONSTRAINT
class Paises(models.Model):
    pais = models.CharField(max_length = 50, unique=True)
    continente = models.CharField(max_length = 10)
    def __str__(self):
         return "{}".format(self.pais) #manera en que visualizamos el objeto en el admin