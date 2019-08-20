from django import forms
from apps.detalleordenpedido.models import DetallePedido

class DetallePedidoForm(forms.ModelForm):

    class Meta:
        model = DetallePedido

        fields = "__all__"

        labels = {
            'cod_producto': 'Codigo producto',
            'cantidad': 'Cantidad',
            'precio_venta': 'Precio de venta',
            'importe': 'Importe',
        }

    def __init__(self, *args, **kwargs):
        super(DetallePedidoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})