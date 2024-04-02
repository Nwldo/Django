from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Aluno, Professor

def novo_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        aluno = Aluno.objects.create(nome=nome)
        return JsonResponse({'id': aluno.id, 'nome': aluno.nome})

def listar_alunos(request):
    alunos = Aluno.objects.all()
    data = [{'id': aluno.id, 'nome': aluno.nome} for aluno in alunos]
    return JsonResponse(data, safe=False)

def detalhes_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    data = {'id': aluno.id, 'nome': aluno.nome}
    return JsonResponse(data)

def remover_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return JsonResponse({'message': 'Aluno removido com sucesso'})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'PUT':
        nome = request.POST.get('nome')
        aluno.nome = nome
        aluno.save()
        return JsonResponse({'message': 'Aluno atualizado com sucesso'})
