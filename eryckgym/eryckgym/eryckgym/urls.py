
from django.contrib import admin
from django.urls import path
from treinos.views import ListaExerciciosView, ExeciciosUpdateAPIView
from cadastro.views import novo_aluno, listar_alunos, detalhes_aluno, remover_aluno, editar_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/exercicios', ListaExerciciosView.as_view()),
    path('api/exercicios/<int:pk>/', ExeciciosUpdateAPIView.as_view(),),
    path('alunos/', listar_alunos),
    path('alunos/novo/', novo_aluno),
]
