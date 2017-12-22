from django.contrib import admin
from .models import Departamento, Ciudad, Sitio

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(Sitio)