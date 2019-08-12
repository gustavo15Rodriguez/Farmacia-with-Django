from django.db import models
from apps.producto.models import Producto

class DetallePedido(models.Model):
    cod_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #nom_producto = models.CharField(max_length=15)
    cantidad = models.IntegerField()
    precio_venta = models.IntegerField()
    importe = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.cod_producto)
