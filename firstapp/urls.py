
from django.urls import path
from firstapp import views
from django.conf.urls import include

urlpatterns = [
    
    #2.3 para la subruta /firstapp/app se ejecuta el metodo otro de views.py
    path('app/',views.otro,name='otro'),
    #f2.3 (firstapp/views.py)
    
    #3.5 para la subruta /firstapp/ se ejecuta el metodo pagina_web de views.py
    path('',views.pagina_web,name='pagina_web'),
    #f3.5 (firstapp/views.py)

    #4.5 para la subruta /firstapp/estatica se ejecuta el metodo muestrababy de views.py
    path('estatica/',views.muestrababy,name='muestrababy'),
    #f4.5 (firstapp/views.py)
    
]