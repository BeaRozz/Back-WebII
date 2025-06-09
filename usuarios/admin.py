from django.contrib import admin

from .models import Usuario;
from .models import TokenUsuario

admin.site.register(Usuario)
admin.site.register(TokenUsuario)