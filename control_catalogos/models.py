from django.db import models

# Create your models here.
class Paises(models.Model):
    pais = models.CharField(max_length = 50, unique=True)
    def __str__(self):
         return "{}".format(self.pais)