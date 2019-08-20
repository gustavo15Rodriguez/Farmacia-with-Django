from django.db import models
from apps.distrito.models import Distrito
from django.utils.translation import ugettext as _

class Clientes(models.Model):
    cod_cliente = models.IntegerField(primary_key=True)
    nom_cliente = models.CharField(max_length=15)
    dir_cliente = models.CharField(max_length=10)
    cod_distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=10)
    dni = models.CharField(max_length=10)
    ruc = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return '{}'.format(self.nom_cliente)

    class Meta:
        permissions = {
            ('cliente_permission', _('Usuario_cliente')),
        }
