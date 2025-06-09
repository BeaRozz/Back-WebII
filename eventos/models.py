from django.db import models
from datetime import time
from fundaciones.models import Fundacion
from lugares.models import Lugar
from categorias.models import Categoria
from img_promocionales.models import Img_Promocional

class Evento(models.Model):
    fundacion = models.ForeignKey(Fundacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    
    fecha_inicial = models.DateField()
    hora_inicial = models.TimeField(default=time(0, 0))

    fecha_final = models.DateField()
    hora_final = models.TimeField(default=time(0, 0))
    
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Img_Promocional, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
