from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fundacion
from .serializers import FundacionSerializer

@api_view(['GET'])
def lista_fundaciones(request):
    fundaciones = Fundacion.objects.all()
    serializer = FundacionSerializer(fundaciones, many=True)
    return Response(serializer.data)
