
from django.contrib import admin
from django.urls import path, include
#from treinos.views import ListaExerciciosView, ExeciciosUpdateAPIView
#from cadastro.views import ListaAlunosView, AlunosUpdateAPIView, ListaProfessorView, ProfessoresUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cadastro.urls')),
    #path('api/exercicios', ListaExerciciosView.as_view()),
    #path('api/exercicios/<int:pk>/', ExeciciosUpdateAPIView.as_view(),),
    #path('api/alunos', ListaAlunosView.as_view()),
    #path('api/alunos/<int:pk>/', AlunosUpdateAPIView.as_view()),
    #path('api/professores', ListaProfessorView.as_view()),
    #path('api/professores/<int:pk>/', ProfessoresUpdateAPIView.as_view()),
]
