from rest_framework import serializers
from .models import Img_Promocional

class ImgPromocionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img_Promocional
        fields = '__all__'