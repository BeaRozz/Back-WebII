from django.urls import path
from .views import lista_fundaciones

urlpatterns = [
    path('fundaciones/', lista_fundaciones, name='lista_fundaciones'),
]
