from django.db import models

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()

    def __str__(self):
        return self.data_emprestimo
