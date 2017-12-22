#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Departamento, Ciudad, Sitio
from forms import ContactenosForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def gracias(request):
    context = {}
    return render(request, 'gracias.html', context)

def nosotros(request):
    context = {}
    return render(request, 'nosotros.html', context)

def sitios(request):
    context = {}
    return render(request, 'sitios.html', context)

def contactenos(request):
    if request.method=='POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        mensaje = request.POST['mensaje'] 

        body_message = "Nombre: " + nombre.upper() + "\n" + "Correo: " + correo + "\n" + "Mensaje: " + mensaje
        
        send_mail('Mensaje de usuario Guía Turística', body_message, 'cmauricio10@gmail.com', ['amcaicedo@unimayor.edu.co'])

    context = {}
    return render(request, 'contactenos.html', context)

class SitioList(ListView):
    model = Sitio
    template_name = 'sitios.html'