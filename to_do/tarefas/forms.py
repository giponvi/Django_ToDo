from django import forms

class formularioTarefa(forms.Form):
    nome = forms.CharField(max_length = 25)
    descricao = forms.CharField()
    status = forms.BooleanField(required = False)


