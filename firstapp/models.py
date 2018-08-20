from django.db import models

# Create your models here.

#5.2 se crean los modelos como clases, despues de creadas ustede debe efectuar la migracion
#con python manage.py migrate y crear los modelos con python manage.py makemigrations

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)
    #no admite duplicados

    def __str__(self):
        return self.top_name
    #se obtiene una version string del modelo

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,  on_delete=models.CASCADE)
    name= models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.CharField(max_length=264,unique=True)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
#f5.2(firstapp/admin.py)




 