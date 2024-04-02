
from django.contrib import admin
from django.urls import path
from treinos.views import ListaExerciciosView, ExeciciosUpdateAPIView
from cadastro.views import ListaAlunosView, AlunosUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/exercicios', ListaExerciciosView.as_view()),
    path('api/exercicios/<int:pk>/', ExeciciosUpdateAPIView.as_view(),),
    path('api/alunos', ListaAlunosView.as_view()),
    path('api/alunos/<int:pk>/', ListaAlunosView.as_view()),
]
