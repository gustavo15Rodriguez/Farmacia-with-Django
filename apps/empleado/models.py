from django.db import models
from apps.distrito.models import Distrito

class Empleado(models.Model):
    cod_empleado = models.CharField(primary_key=True, max_length=6)
    nom_empleado = models.CharField(max_length=15)
    dir_empleado = models.CharField(max_length=15)
    cod_distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=10)
    edad = models.IntegerField(max_length=5)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return '{}'.format(self.nom_empleado)