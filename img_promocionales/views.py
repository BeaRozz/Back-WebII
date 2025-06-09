from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from usuarios.auth import TokenAuthPermission
from .models import Img_Promocional
from .serializers import ImgPromocionalSerializer

@api_view(['GET'])
@permission_classes([TokenAuthPermission])
def lista_img_promocionales(request):
    img = Img_Promocional.objects.all()
    serializer = ImgPromocionalSerializer(img, many=True)
    return Response(serializer.data)