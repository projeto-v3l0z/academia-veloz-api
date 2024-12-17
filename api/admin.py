from django.contrib import admin

from accounts.models import User
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(TipoCurso)