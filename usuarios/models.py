import uuid
from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=125, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class TokenUsuario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f"{self.usuario.email} - Token"
