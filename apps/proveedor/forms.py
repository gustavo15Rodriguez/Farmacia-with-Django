from django import forms
from apps.proveedor.models import Proveedor

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor

        fields = "__all__"

        labels = {
            'cod_proveedor': 'Codigo',
            'nom_proveedor': 'Nombre del proveedor',
            'dir_proveedor': 'Direccion',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'id_distrito': 'Distrito',
        }

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})