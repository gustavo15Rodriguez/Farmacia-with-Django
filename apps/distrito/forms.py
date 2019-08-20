from apps.distrito.models import Distrito
from django import forms

class DistritoForm(forms.ModelForm):

    class Meta:
        model = Distrito

        fields = "__all__"

        labels = {
            'cod_distrito': 'Codigo',
            'nom_distrito': 'Nombre del distrito',
        }

    def __init__(self, *args, **kwargs):
        super(DistritoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})