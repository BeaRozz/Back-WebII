from rest_framework.permissions import BasePermission
from .models import TokenUsuario

class TokenAuthPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        if not token:
            return False
        token = token.replace('Token ', '')
        return TokenUsuario.objects.filter(token=token).exists()
