from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Bienvenido')

def contacto(request):
    return render(request,'paginas/nosotros.html')