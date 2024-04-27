# no codigo comentado ele mostra apenas os dados de id e nome, porem esses dados eu defino na mão e não pego do banco
#no codigo em execução eu ja começo a pegar os dados do banco, com a ajuda do arquivo serializar.py
#from django.http import JsonResponse
#
#def alunos(request):
#    if request.method == 'GET':
#        aluno = {'id':1, 'nome': 'Felipe'}
#        return JsonResponse(aluno)
#

from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosManitruladosEmUmCurso

#responsavel por autenticar a chamada da API
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all() #traz todos os alunos do bd
    serializer_class = AlunoSerializer #classe responsavel que traz os alunos
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosManitruladosEmUmCurso
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    