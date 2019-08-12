from django.db import models

class Categoria(models.Model):
    cod_categoria = models.IntegerField(primary_key=True)
    nom_categoria = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.nom_categoria)
