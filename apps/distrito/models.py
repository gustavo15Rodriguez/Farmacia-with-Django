from django.db import models

class Distrito(models.Model):
    cod_distrito = models.IntegerField(primary_key=True)
    nom_distrito = models.CharField(max_length=15)

    def __str__(self):
        return '{}'.format(self.nom_distrito)
