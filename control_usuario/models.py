from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

#Usamos el modelo de usarios que tiene por defecto django
class User(AbstractUser):
    def __str__(self):
         return "{}".format(self.username)