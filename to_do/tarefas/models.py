from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 150)
    data_criacao = models.DateTimeField(auto_now_add=True)
    choices = (
        ('Pendente', 'Pendente'),
        ('Iniciada', 'Iniciada'),
        ('Concluída', 'Concluída')
        )
    status = models.CharField(max_length = 9, choices = choices, default = 'Pendente')

    def __str__(self):
        return self.nome