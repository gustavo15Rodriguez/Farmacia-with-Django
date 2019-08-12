from django.db import models
from apps.clientes.models import Clientes
from apps.empleado.models import Empleado

class OrdenPedido(models.Model):
    num_pedido = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    cod_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    #nom_cliente = models.CharField(max_length=12)
    cod_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cod_tipo_pago = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.fecha, self.cod_cliente)
