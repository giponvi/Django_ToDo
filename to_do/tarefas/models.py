from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length = 25)
    descricao = models.CharField()
    status = models.BooleanField()

    def __str__(self):
        return self.nome