
from django.contrib import admin
from django.urls import path
from treinos.views import ListaExerciciosView, ExeciciosUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/exercicios', ListaExerciciosView.as_view()),
    path('api/exercicios/<int:pk>/', ExeciciosUpdateAPIView.as_view(),),
]
