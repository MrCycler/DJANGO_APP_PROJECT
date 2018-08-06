"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from firstapp import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    #1.3 Se importa el archivo views de first app, una llamada a la pagina principal lanza el metodo index
    path('',views.index,name='index'),
    #f1.3 (first_project/settings.py)

    #2.2 para la ruta /firstapp se cargan otras rutas /firstapp/otras descritas en el archivo incluido
    path('firstapp/', include('firstapp.urls')),
    #f2.2 (firstapp/urls.py)
]
