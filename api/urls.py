from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import TipoCursoListCreateView, TipoCursoRetrieveUpdateDestroyView
router = DefaultRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('tipos-curso/', TipoCursoListCreateView.as_view(), name='tipos-curso-list-create'),
    path('tipos-curso/<int:pk>/', TipoCursoRetrieveUpdateDestroyView.as_view(), name='tipos-curso-detail'),

]