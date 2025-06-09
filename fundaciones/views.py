# eventos/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Fundacion
from .serializers import FundacionSerializer
from rest_framework import status

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_fundaciones(request):
    fundaciones = Fundacion.objects.all()
    serializer = FundacionSerializer(fundaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def detalle_fundacion(request, id):
    try:
        fundacion = Fundacion.objects.get(id=id)
    except Fundacion.DoesNotExist:
        return Response(
            {"error": f"No se encontró la fundación con ID {id}"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": "Error inesperado", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    serializer = FundacionSerializer(fundacion)
    return Response(serializer.data)