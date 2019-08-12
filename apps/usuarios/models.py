from django.db import models
'''from apps.empleado.models import Empleado

class Usuario(models.Model):
    cod_usuario = models.IntegerField(primary_key=True)
    cod_empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    nivel_usuario = models.CharField(max_length=12)
    nom_usuario = models.CharField(max_length=12)
    password = models.CharField(max_length=15)
    activo = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.nom_usuario)'''