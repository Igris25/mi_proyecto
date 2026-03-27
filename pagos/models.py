from django.db import models

class Pago(models.Model):
    usuario = models.CharField(max_length=100)
    monto = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario