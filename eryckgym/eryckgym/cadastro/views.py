
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cadastro.serializers import AlunoSerializer,ProfessorSerializer
from cadastro.models import Aluno, Professor

# CBV --> Class Based View | Aluno
class ListaAlunosView(APIView):

    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class AlunosUpdateAPIView(APIView):
    def get_object(self, pk):
            try:
                return Aluno.objects.get(pk=pk)
            except Aluno.DoesNotExist:
                raise Http404
    
    def get(self, request, pk):
        alunos = self.get_object(pk)
        serializer = AlunoSerializer(alunos)
        return Response(serializer.data)
    
    def put(self, request, pk):
        alunos = self.get_object(pk)
        serializer = AlunoSerializer(alunos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        alunos = self.get_object(pk)
        alunos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# CBV --> Class Based View | Professor
class ListaProfessorView(APIView):

    def get(self, request):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class ProfessoresUpdateAPIView(APIView):
    def get_object(self, pk):
            try:
                return Professor.objects.get(pk=pk)
            except Professor.DoesNotExist:
                raise Http404
    
    def get(self, request, pk):
        professores = self.get_object(pk)
        serializer = ProfessorSerializer(professores)
        return Response(serializer.data)
    
    def put(self, request, pk):
        professores = self.get_object(pk)
        serializer = ProfessorSerializer(professores, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        professores = self.get_object(pk)
        professores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
