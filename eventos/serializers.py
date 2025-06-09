from rest_framework import serializers
from .models import Evento
from fundaciones.serializers import FundacionSerializer
from lugares.serializers import LugarSerializer
from categorias.serializers import CategoriaSerializer
from img_promocionales.serializers import ImgPromocionalSerializer

from eventos.models import Evento
from fundaciones.models import Fundacion
from lugares.models import Lugar
from categorias.models import Categoria
from img_promocionales.models import Img_Promocional
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

# Serializador para eventos con detalles completos
class EventoSerializer(serializers.ModelSerializer):
    fundacion = FundacionSerializer()
    imagen = ImgPromocionalSerializer()
    lugar = LugarSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Evento
        fields = '__all__'

        
#Serializador para crear eventos con validaciones específicas igual edita
class EventoSerializerCreate(serializers.ModelSerializer):
    fundacion = serializers.CharField()
    lugar = serializers.CharField()
    categoria = serializers.CharField()
    imagen = serializers.CharField()

    class Meta:
        model = Evento
        fields = [
            'nombre', 'descripcion',
            'fecha_inicial', 'hora_inicial',
            'fecha_final', 'hora_final',
            'fundacion', 'lugar', 'categoria', 'imagen'
        ]

    def validate(self, data):
        # Validaciones de campos vacíos
        if not data['nombre'].strip():
            raise serializers.ValidationError({"nombre": "El nombre no puede estar vacío"})
        if not data['descripcion'].strip():
            raise serializers.ValidationError({"descripcion": "La descripción no puede estar vacía"})

        # Validar que la combinación de fecha y hora inicial < final
        dt_inicio = datetime.combine(data['fecha_inicial'], data['hora_inicial'])
        dt_final = datetime.combine(data['fecha_final'], data['hora_final'])

        if dt_inicio >= dt_final:
            raise serializers.ValidationError("La fecha y hora inicial deben ser anteriores a la final")

        return data

    def create(self, validated_data):
        fundacion_nombre = validated_data.pop('fundacion')
        lugar_nombre = validated_data.pop('lugar')
        categoria_nombre = validated_data.pop('categoria')
        imagen_nombre = validated_data.pop('imagen')

        from django.shortcuts import get_object_or_404

        fundacion = get_object_or_404(Fundacion, nombre=fundacion_nombre)
        lugar = get_object_or_404(Lugar, nombre=lugar_nombre)
        categoria = get_object_or_404(Categoria, nombre=categoria_nombre)
        imagen = get_object_or_404(Img_Promocional, nombre=imagen_nombre)

        evento = Evento.objects.create(
            fundacion=fundacion,
            lugar=lugar,
            categoria=categoria,
            imagen=imagen,
            **validated_data
        )
        return evento
    
    def update(self, instance, validated_data):
        fundacion_nombre = validated_data.pop('fundacion')
        lugar_nombre = validated_data.pop('lugar')
        categoria_nombre = validated_data.pop('categoria')
        imagen_nombre = validated_data.pop('imagen')

        if fundacion_nombre:
            instance.fundacion = Fundacion.objects.get(nombre=fundacion_nombre)
        if lugar_nombre:
            instance.lugar = Lugar.objects.get(nombre=lugar_nombre)
        if categoria_nombre:
            instance.categoria = Categoria.objects.get(nombre=categoria_nombre)
        if imagen_nombre:
            instance.imagen = Img_Promocional.objects.get(nombre=imagen_nombre)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance