from django.db import models

class Revista(models.Model):
    numero_edicao = models.IntegerField()
    ano = models.IntegerField

    def __str__(self):
        return self.numero_edicao
