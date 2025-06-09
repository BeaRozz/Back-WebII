from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Usuario, TokenUsuario
import uuid

@api_view(['GET', 'POST'])  # permite ambos métodos
@permission_classes([AllowAny])
def login_usuario(request):
    # Obtener email y password desde los params si son GET
    email = request.query_params.get('email') or request.data.get('email')
    password = request.query_params.get('password') or request.data.get('password')

    if not email or not password:
        return Response({'error': 'Faltan email o contraseña'}, status=400)

    try:
        usuario = Usuario.objects.get(email=email, password=password)
    except Usuario.DoesNotExist:
        return Response({'error': 'Credenciales inválidas'}, status=401)

    from .models import TokenUsuario
    import uuid
    token, creado = TokenUsuario.objects.get_or_create(usuario=usuario)
    if not creado:
        token.token = str(uuid.uuid4())
        token.save()

    return Response({'token': token.token})
