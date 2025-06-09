# eventos/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Fundacion
from .serializers import FundacionSerializer

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_fundaciones(request):
    fundaciones = Fundacion.objects.all()
    serializer = FundacionSerializer(fundaciones, many=True)
    return Response(serializer.data)
