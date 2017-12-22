from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    CALIENTE = 'CA'
    FRIO = 'FR'
    TEMPLADO = 'TE'
    CLIMA_CHOICES = (
        (CALIENTE, 'Caliente'),
        (FRIO, 'Frio'),
        (TEMPLADO, 'Templado'),
    )

    nombre = models.CharField(max_length=100, unique=True)
    habitantes = models.IntegerField()
    clima = models.CharField(
        max_length=2,
        choices=CLIMA_CHOICES,
        default=CALIENTE,
    )
    departamento = models.ForeignKey(Departamento)

    def __unicode__(self):
        return self.nombre

class Sitio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='fotos')
    ciudad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return self.nombre