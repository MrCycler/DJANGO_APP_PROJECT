
from django.urls import path
from firstapp import views
from django.conf.urls import include

urlpatterns = [
 
    path('app/',views.otro,name='otro'),
    
]