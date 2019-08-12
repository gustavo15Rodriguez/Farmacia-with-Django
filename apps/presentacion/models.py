from django.db import models

class Presentacion(models.Model):
    cod_presentacion = models.IntegerField(primary_key=True)
    nom_presentacion = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nom_presentacion)