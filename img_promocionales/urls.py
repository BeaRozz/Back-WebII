from django.urls import path
from .views import lista_img_promocionales

urlpatterns = [
    path('img_promocionales/', lista_img_promocionales),
]