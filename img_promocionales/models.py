from django.db import models

class Img_Promocional(models.Model):
    nombre = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre