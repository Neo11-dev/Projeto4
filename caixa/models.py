from django.db import models

class Caixa(models.Model):
    numero = models.IntegerField()
    etiqueta = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)

    def __str__(self):
        return self.numero
