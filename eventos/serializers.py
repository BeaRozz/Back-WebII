from rest_framework import serializers
from .models import Evento
from fundaciones.serializers import FundacionSerializer
from lugares.serializers import LugarSerializer
from categorias.serializers import CategoriaSerializer
from img_promocionales.serializers import ImgPromocionalSerializer

class EventoSerializer(serializers.ModelSerializer):
    fundacion = FundacionSerializer()
    imagen = ImgPromocionalSerializer()
    lugar = LugarSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Evento
        fields = '__all__'
