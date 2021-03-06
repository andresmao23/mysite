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

def detalle_sitio(request, id_sitio):
    sitio = Sitio.objects.get(id=id_sitio)
    #clima = sitio.ciudad.get_clima_display()
    context = {'sitio':sitio}
    return render(request, 'detalle.html', context)

def contactenos(request):
    if request.method=='POST':
        form = ContactenosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje'] 
            body_message = "Nombre: " + nombre.upper() + "\n" + "Correo: " + correo + "\n" + "Mensaje: " + mensaje
            send_mail('Mensaje de usuario Guía Turística', body_message, 'cmauricio10@gmail.com', ['amcaicedo@unimayor.edu.co'])
            return redirect('gracias')
    else:
        form = ContactenosForm()
    
    context = {'form':form}
    return render(request, 'contactenos.html', context)

class SitioList(ListView):
    model = Sitio
    template_name = 'sitios.html'
    paginate_by = 3