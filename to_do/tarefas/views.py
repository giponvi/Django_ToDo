from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formularioTarefa
from .models import Tarefa

def home(request):
    nome = 'Giovane'
    return render(request, 'home.html', {'nome':nome })

def ver_tarefas(request):
    return render(request, 'ver_tarefas.html')

def criar_tarefas(request):
    if request.method == "GET":
        form = formularioTarefa()
        return render(request, 'criar_tarefas.html', {'form':form})
    elif request.method == "POST":
        id = request.POST.get('id')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if request.POST.get('status'):
            status = True
        else:
            status = False

        tarefa = Tarefa(id, nome, descricao, status)
        tarefa.save()
        return  redirect('home')

def deletar_tarefas(request):
    return HttpResponse("Deletando tarefas")

def atualizar_tarefas(request):
    return HttpResponse("Atualizando tarefas")