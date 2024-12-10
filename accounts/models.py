from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    complete_name = models.CharField(max_length=100)
    instituicao = models.ForeignKey('api_emblema.Instituicao', on_delete=models.CASCADE, null=True, blank=True)
    REQUIRED_FIELDS = ['complete_name', 'username']
    USERNAME_FIELD = 'email'
    pass

