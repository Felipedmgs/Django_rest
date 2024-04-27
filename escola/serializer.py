from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        #aqui defino qual campo vai estar na api
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        #podemos disponibilizar todos os dados co o all na api
        fields = '__all__'
        
        
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #se deixar vazio eu pega todos os campos
        
        
class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
        
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosManitruladosEmUmCurso(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
    
        
        