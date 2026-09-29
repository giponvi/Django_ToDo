from django.shortcuts import render
from django.http import HttpResponse


def ver_tarefas(request):
    nome = 'Giovane'
    return render(request, 'ver_tarefas.html', {'nome':nome })

def criar_tarefas(request):
    return HttpResponse("Criando tarefas")

def deletar_tarefas(request):
    return HttpResponse("Deletando tarefas")

def atualizar_tarefas(request):
    return HttpResponse("Atualizando tarefas")