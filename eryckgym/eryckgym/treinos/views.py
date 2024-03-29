from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from treinos.serializers import ExercicioSerializer
from treinos.models import Exercicio

# CBV --> Class Based View
class ListaExerciciosView(APIView):

    def get(self, request):
        exercicios = Exercicio.objects.all()
        serializer = ExercicioSerializer(exercicios, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        serializer = ExercicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class ExeciciosUpdateAPIView(APIView):
    def get_object(self, pk):
            try:
                return Exercicio.objects.get(pk=pk)
            except Exercicio.DoesNotExist:
                raise Http404
    
    def get(self, request, pk):
        exercicios = self.get_object(pk)
        serializer = ExercicioSerializer(exercicios)
        return Response(serializer.data)
    
    def put(self, request, pk):
        exercicios = self.get_object(pk)
        serializer = ExercicioSerializer(exercicios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        exercicios = self.get_object(pk)
        exercicios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)