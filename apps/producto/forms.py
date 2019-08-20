from django import forms
from apps.producto.models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = "__all__"

        labels = {
            'cod_producto': 'Codigo',
            'nom_producto': 'Nombre del producto',
            'pre_venta': 'Precio de venta',
            'pre_compra': 'Precio de compra',
            'fecha_vencimiento': 'Fecha de vencimiento',
            'stock': 'Stock',
            'cod_categoria': 'Categoria',
            'cod_proveedor': 'Proveedor',
            'cod_presentacion': 'Presentacion',
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})