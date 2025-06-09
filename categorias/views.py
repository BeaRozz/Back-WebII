from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Categoria
from .serializers import CategoriaSerializer

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)