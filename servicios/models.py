from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_creditos = models.IntegerField()

    def __str__(self):
        return self.nombre