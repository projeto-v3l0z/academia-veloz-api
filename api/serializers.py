from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import User

from .models import *
from rest_framework import serializers
from .models import Curso, Modulo, Aula

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'complete_name', 'is_active', 'is_staff', 'is_superuser']





class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'

class ModuloSerializer(serializers.ModelSerializer):
    aulas = AulaSerializer(many=True, read_only=True)

    class Meta:
        model = Modulo
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    modulos = ModuloSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'
