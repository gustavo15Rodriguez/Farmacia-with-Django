from django import forms
from apps.presentacion.models import Presentacion

class PresentacionForm(forms.ModelForm):

    class Meta:
        model = Presentacion

        fields = "__all__"

        labels = {
            'cod_presentacion': 'Codigo de la presetacion',
            'nom_presentacion': 'Nombre de la presentacion',
        }

    def __init__(self, *args, **kwargs):
        super(PresentacionForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})