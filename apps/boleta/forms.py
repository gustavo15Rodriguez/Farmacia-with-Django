from django import forms
from apps.boleta.models import Boleta

class BoletaForm(forms.ModelForm):

    class Meta:
        model = Boleta

        fields = "__all__"

        labels = {
            'num_boleta': 'Numero de boleta',
            'fecha': 'Fecha',
            'codi_empleado': 'Codigo del empleado',
            'cod_cliente': 'Codigo el cliente',
            'num_ordenpedido': 'Numero de pedido',
            'subtotal': 'Subtotal',
            'descuento': 'Descuento',
        }

    def __init__(self, *args, **kwargs):
        super(BoletaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})