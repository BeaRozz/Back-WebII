from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Evento
from .serializers import EventoSerializer, EventoSerializerCreate
from rest_framework import status

#Obtener todos los eventos
@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_eventos(request):
    eventos = Evento.objects.all()
    serializer = EventoSerializer(eventos, many=True)
    return Response(serializer.data)

#Obtener evento por ID
@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def detalle_evento(request, id):
    try:
        evento = Evento.objects.get(id=id)
    except Evento.DoesNotExist:
        return Response(
            {"error": f"No se encontró el evento con ID {id}"},
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {"error": "Error inesperado", "detalle": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    serializer = EventoSerializer(evento)
    return Response(serializer.data)

#Crear un nuevo evento
@api_view(['POST'])
@permission_classes([TokenAuthPermission])
def crear_evento(request):
    serializer = EventoSerializerCreate(data=request.data)
    if serializer.is_valid():
        try:
            evento = serializer.save()
            return Response(EventoSerializer(evento).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                {"error": "Error al crear evento", "detalle": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)