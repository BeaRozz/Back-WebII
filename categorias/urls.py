from django.urls import path
from .views import lista_categorias

urlpatterns = [
    path('categorias/', lista_categorias),
]