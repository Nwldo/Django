from rest_framework import serializers
from cadastro.models import Aluno, Professor

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Aluno
        fields = ['id', 'nome', 'sexo', 'idade', 'cpf', 'telefone', 'treino']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model: Professor
        fields = ['id', 'nome', 'especialidade', 'treinos']