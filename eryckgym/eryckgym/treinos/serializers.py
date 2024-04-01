from rest_framework.serializers import ModelSerializer
from treinos.models import Exercicio, Treino


class ExercicioSerializer(ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'descricao',
                  'em_equipamento', 'idade_minima_aluno']

class TreinoSerializer(ModelSerializer):
    class Meta:
        model: Treino
        fields = ['id', 'nome', 'Exercicios']