from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('criar_tarefas', views.criar_tarefas, name = 'criar_tarefas'),
    path('ver_tarefas', views.ver_tarefas, name = 'ver_tarefas'),
    path('atualizar_tarefas/<int:id>', views.atualizar_tarefas, name = 'atualizar_tarefas'),
    path('deletar_tarefas/<int:id>', views.deletar_tarefas, name = 'deletar_tarefas')    
]
