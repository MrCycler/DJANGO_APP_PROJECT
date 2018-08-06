from django.shortcuts import render
from django.http import HttpResponse

#1.2 se crea una funcion que va a manejar la vista, en este caso esta funcion responde a la llamada con 
#una linea html
def index(request):
    return HttpResponse("<em>Hello my friend</em>")
	# Html response
##f1.2 (first_project/urls.py)

#2.4 Metodo que responde a la llamada desde la subruta, ejecutar aca acaba
def otro(request):
    return HttpResponse("<em>Not today</em>")
#f2.4ft


#3.6 Metodo que responde a la llamada desde la subruta, en la variable de contexto se da
#valor a la variable que estaba encerrada en corchetes en el html
#se usa render para renderizar la pagina html, ejecutar
def pagina_web(request):
    my_dict ={'elementoinsertado':"Me inserto en first_app/views.py"}
    return render(request,'firstapp/pagina.html',context=my_dict)
#f3.6ft

