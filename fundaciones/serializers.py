from rest_framework import serializers
from .models import Fundacion

class FundacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fundacion
        fields = '__all__'
