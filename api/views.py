import logging
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import *
from rest_framework.decorators import action
from django.db import transaction
# Create your views here.
from rest_framework import generics
from .models import TipoCurso
from .serializers import TipoCursoSerializer
logger = logging.getLogger(__name__)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get']

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({
                'message': 'Email e senha são obrigatórios.'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                'message': 'Usuário com esse email não encontrado.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({
                'message': 'Usuário inativo.'
            }, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({
                'message': 'Senha incorreta.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        last_login = user.last_login
        
        refresh = RefreshToken.for_user(user)
        
        user.last_login = timezone.now()
        user.save()

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'id': user.id,
            'username': user.username,
            'last_login': last_login,
        }, status=status.HTTP_200_OK)

class UserTokenRefreshView(TokenRefreshView):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        email = self.request.query_params.get('email')
        
        if username:
            queryset = queryset.filter(username__icontains=username)
        if email:
            queryset = queryset.filter(email__icontains=email)
        
        return queryset
    
class TipoCursoViewSet(viewsets.ModelViewSet):
    queryset = TipoCurso.objects.all()
    serializer_class = TipoCursoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        queryset = TipoCurso.objects.all()
        nome = self.request.query_params.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        
        
        return queryset
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        queryset = Curso.objects.all()
        tipo = self.request.query_params.get('tipo')
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        return queryset

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
    permission_classes = [IsAuthenticated]

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    permission_classes = [IsAuthenticated]
