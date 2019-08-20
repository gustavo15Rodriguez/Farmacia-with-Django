from django.db import models
from apps.distrito.models import Distrito
from django.utils.translation import ugettext as _

class Proveedor(models.Model):
    cod_proveedor = models.CharField(primary_key=True, max_length=6)
    nom_proveedor = models.CharField(max_length=15)
    dir_proveedor = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)
    id_distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nom_proveedor)

    class Meta:
        permissions = {
            ('proveedor_permission', _('Usuario proveedor')),
        }