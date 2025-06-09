from django.urls import path
from .views import lista_lugares

urlpatterns = [
    path('lugares/', lista_lugares),
]