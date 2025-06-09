from django.urls import path
from .views import lista_eventos, detalle_evento, crear_evento

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>/', detalle_evento, name='detalle_evento'),
    path('eventos/crear/', crear_evento, name='crear_evento'),
]
