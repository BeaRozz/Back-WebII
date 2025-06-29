"""
URL configuration for APIdonaciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import login_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', login_usuario, name='login_usuario'),
    path('api/', include('fundaciones.urls')),
    path('api/', include('categorias.urls')),
    path('api/', include('img_promocionales.urls')),
    path('api/', include('lugares.urls')),
    path('api/', include('eventos.urls')),
]
