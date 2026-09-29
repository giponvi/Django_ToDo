from django.urls import path
from . import views

urlpatterns = [
    path('criar_tarefas', views.criar_tarefas, name = 'criar tarefas'),
    path('ver_tarefas', views.ver_tarefas, name = 'ver_tarefas'),
    path('atualizar_tarefas', views.atualizar_tarefas, name = 'atualizar_tarefas'),
    path('deletar_tarefas', views.deletar_tarefas, name = 'deletar_tarefas')    
]
