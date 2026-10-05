from .models import Tarefa
from django import forms

class formularioTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'status',]

