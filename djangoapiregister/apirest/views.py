from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Register
from .serializers import RegisterSerializer

class RegisterListAPIView(APIView):
    def get(self, request):
        users = Register.objects.all()
        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RegisterUpdateAPIView(APIView):
    def get_object(self, pk):
        try:
            return Register.objects.get(pk=pk)
        except Register.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = RegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)