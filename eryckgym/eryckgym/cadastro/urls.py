
from django.urls import path
from cadastro.views import ListaAlunosView, AlunosUpdateAPIView, ListaProfessorView, ProfessoresUpdateAPIView

urlpatterns = [
    path('api/alunos', ListaAlunosView.as_view(), name='listar_alunos'),
    path('api/alunos/<int:pk>/', AlunosUpdateAPIView.as_view()),
    path('api/professores', ListaProfessorView.as_view()),
    path('api/professores/<int:pk>/', ProfessoresUpdateAPIView.as_view()),
]