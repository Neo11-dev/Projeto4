from django.db import models

class Amigo(models.Model):
    nome = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    grupo_amigo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
