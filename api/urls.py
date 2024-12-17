from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('tipo-curso', TipoCursoViewSet, basename='tipoCurso')

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]