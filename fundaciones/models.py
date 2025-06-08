from django.db import models

class Fundacion(models.Model):
    nombre = models.CharField(max_length=100)
    mision = models.CharField(max_length=255)
    areas_enfoque = models.CharField(max_length=255)
    link_logo = models.CharField(max_length=255)
    proyectos_destacados = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre