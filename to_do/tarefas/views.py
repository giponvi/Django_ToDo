from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import formularioTarefa
from .models import Tarefa

def home(request):
    nome = 'Giovane'
    return render(request, 'home.html', {'nome':nome })

def ver_tarefas(request):
    contexto = {
        "nome": "01",
        "tarefas": Tarefa.objects.all()
    }
    return render(request, 'ver_tarefas.html', contexto)

def criar_tarefas(request):
    if request.method == "GET":
        form = formularioTarefa()
        return render(request, 'criar_tarefas.html', {'form': form})
    elif request.method == "POST":
        form = formularioTarefa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'criar_tarefas.html', {'form': form})

def deletar_tarefas(request, id):
    if request.method == "POST":
        deletar = get_object_or_404(Tarefa, id=id)
        deletar.delete()
        return redirect('ver_tarefas')

def atualizar_tarefas(request, id):
    atualizar = get_object_or_404(Tarefa, id=id)
    if request.method == "POST":
        form = formularioTarefa(request.POST, instance = atualizar)
        if form.is_valid():
            form.save()
            return redirect('ver_tarefas')
    formulario = formularioTarefa(instance = atualizar)
    contexto = {
        'form':formulario
    }
    return render(request, 'atualizar_tarefa.html', contexto)
  