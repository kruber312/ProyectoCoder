from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40) #Para la base de datos un string es un CharField
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return f'Curso: {self.nombre}, Camada: {self.camada}'
