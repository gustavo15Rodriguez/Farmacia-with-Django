from django import forms
from apps.categoria.models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        fields = "__all__"

        labels = {
            'cod_categoria': 'Codigo de la categoria',
            'nom_categoria': 'Nombre',
        }

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})