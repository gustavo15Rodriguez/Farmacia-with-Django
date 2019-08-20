from django import forms
from apps.clientes.models import Clientes

class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes

        fields = "__all__"

        labels = {
            'cod_cliente': 'Codigo del cliente',
            'nom_cliente': 'Nombre',
            'dir_cliente': 'Direccion',
            'cod_distrito': 'Distrito',
            'sexo': 'Sexo',
            'dni': 'DNI',
            'ruc': 'RUC',
            'telefono': 'Telefono',
            'celular': 'Celular',
        }

    def __init__(self, *args, **kwargs):
        super(ClientesForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})