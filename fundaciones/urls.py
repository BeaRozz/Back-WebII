from django.urls import path
from .views import lista_fundaciones, detalle_fundacion

urlpatterns = [
    path('fundaciones/', lista_fundaciones),
    path('fundaciones/<int:id>/', detalle_fundacion),
]

