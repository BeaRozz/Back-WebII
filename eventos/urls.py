from django.urls import path
from .views import lista_eventos, detalle_evento, crear_evento, editar_evento, eliminar_evento

urlpatterns = [
    path('eventos/', lista_eventos, name='lista_eventos'),
    path('eventos/<int:id>/', detalle_evento, name='detalle_evento'),
    path('eventos/crear/', crear_evento, name='crear_evento'),
    path('eventos/<int:id>/editar/', editar_evento, name='editar_evento'),
    path('eventos/<int:id>/eliminar/', eliminar_evento, name='eliminar_evento'),
]
