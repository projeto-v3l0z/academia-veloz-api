from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import User

from .models import *
from rest_framework import serializers
from .models import TipoCurso

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'complete_name', 'is_active', 'is_staff', 'is_superuser']



class TipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCurso
        fields = '__all__'
