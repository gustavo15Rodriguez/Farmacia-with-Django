from django import forms
from apps.ordenpedido.models import OrdenPedido

class OrdenPedidoForm(forms.ModelForm):

    class Meta:
        model = OrdenPedido

        fields = "__all__"

        labels = {
            'num_pedido': 'Numero de pedido',
            'fecha': 'Fecha',
            'cod_cliente': 'Codigo del cliente',
            'cod_empleado': 'Codigo del empleado',
            'cod_tipo_pago': 'Tipo de pago',
            'total': 'Total a pagar',
        }

    def __init__(self, *args, **kwargs):
        super(OrdenPedidoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})