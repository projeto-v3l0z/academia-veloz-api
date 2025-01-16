from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from accounts.models import User
from .models import *
from rest_framework import serializers
from .models import Curso, Modulo, Aula

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'complete_name', 'is_active', 'is_staff', 'is_superuser']

class AulaConcluidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AulaConcluida
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ArquivoAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArquivoAula
        fields = '__all__'

class AulaSerializer(serializers.ModelSerializer):
    arquivos = ArquivoAulaSerializer(many=True, read_only=True)
    conclusoes = AulaConcluidaSerializer(many=True, read_only=True)

    class Meta:
        model = Aula
        fields = '__all__'

class CursoModuloSerializer(serializers.ModelSerializer):
    matriculas = MatriculaSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'

class ModuloSerializer(serializers.ModelSerializer):    
    # Para ler uso todo o objeto
    aulas = AulaSerializer(many=True, read_only=True)
    curso = CursoModuloSerializer(read_only=True)

    # para post uso apenas o id
    curso_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modulo
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    # Para ler uso todo o objeto
    modulos = ModuloSerializer(many=True, read_only=True)
    alunos = UserSerializer(many=True, read_only=True)
    
    # para post uso apenas o id
    alunos_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.all(), 
        source='alunos',
    )

    class Meta:
        model = Curso
        fields = '__all__'