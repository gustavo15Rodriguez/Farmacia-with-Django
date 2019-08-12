from django.db import models
from apps.categoria.models import Categoria
from apps.proveedor.models import Proveedor
from apps.presentacion.models import Presentacion

class Producto(models.Model):
    cod_producto = models.IntegerField(primary_key=True)
    nom_producto = models.CharField(max_length=15)
    pre_venta = models.IntegerField()
    pre_compra = models.IntegerField()
    fecha_vencimiento = models.DateField()
    stock = models.CharField(max_length=10)
    cod_categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    cod_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cod_presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nom_producto)