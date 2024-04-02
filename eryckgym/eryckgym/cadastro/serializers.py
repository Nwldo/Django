from rest_framework.serializers import ModelSerializer
from cadastro.models import Aluno, Professor

class AlunoSerializer(ModelSerializer):
    class Meta:
        model: Aluno
        fields = ['id', 'nome', 'sexo', 'idade', 'cpf', 'telefone', 'treino']

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model: Professor
        fields = ['id', 'nome', 'especialidade', 'treinos']