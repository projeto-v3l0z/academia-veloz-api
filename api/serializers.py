from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from accounts.models import User

from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'complete_name', 'is_active', 'is_staff', 'is_superuser']