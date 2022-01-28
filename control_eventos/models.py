from django.db import models

# Create your models here.
class Eventos(models.Model):
    # departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    evento = models.CharField(max_length = 200)
    fecha = models.CharField(max_length = 50)
    hora = models.CharField(max_length = 50)
    def __str__(self):
         return "{}".format(self.evento)