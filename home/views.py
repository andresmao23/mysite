from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def nosotros(request):
    context = {}
    return render(request, 'nosotros.html', context)

def sitios(request):
    context = {}
    return render(request, 'sitios.html', context)

def contactenos(request):
    context = {}
    return render(request, 'contactenos.html', context)