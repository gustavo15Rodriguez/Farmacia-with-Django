from django.db import models
from apps.empleado.models import Empleado
from apps.clientes.models import Clientes

class Boleta(models.Model):
    num_boleta = models.CharField(max_length=12, primary_key=True)
    fecha = models.EmailField()
    codi_empleado = models.ForeignKey(Empleado, null=True, blank=True, on_delete=models.CASCADE)
    cod_cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
    num_ordenpedido = models.IntegerField()
    subtotal = models.IntegerField()
    descuento = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.fecha)
