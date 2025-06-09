from django.urls import path
from .views import lista_eventos, detalle_evento

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>/', detalle_evento, name='detalle_evento'),
]
