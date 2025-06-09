from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Lugar
from .serializers import LugarSerializer

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_lugares(request):
    lugar = Lugar.objects.all()
    serializer = LugarSerializer(lugar, many=True)
    return Response(serializer.data)