from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>Hello my friend</em>")
	# Html response

def otro(request):
    return HttpResponse("<em>Not today</em>")

