from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def coraje(request):
    return render(request, "core/coraje.html")

def doraemon(request):
    return render(request, "core/doraemon.html")

def garfield(request):
    return render(request, "core/garfield.html")

def gatos(request):
    return render(request, "core/gatos.html")

def patan(request):
    return render(request, "core/patan.html")

def perros(request):
    return render(request, "core/perros.html")

def scooby(request):
    return render(request, "core/scooby.html")

def tom(request):
    return render(request, "core/tom.html")