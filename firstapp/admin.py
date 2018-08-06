from django.contrib import admin
from firstapp.models import Topic,WebPage, AccessRecord
# Register your models here.
#5.3 se registran los modelos de la aplicacion, para acceder a esta info requiere un superusuario creado con
# python manage.py createsuperuser
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)
#f5.3ft
