from django import forms
from apps.empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado

        fields = "__all__"

        labels = {
            'cod_empleado': 'Codigo',
            'nom_empleado': 'Nombre del empleado',
            'dir_empleado': 'Direccion',
            'cod_distrito': 'Distrito',
            'cargo': 'Cargo',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'celular': 'Celular',
        }

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form_control'})