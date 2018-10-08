# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TiposDeServicio(models.Model):
    nombre = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='services', null=True)

    def __unicode__(self):
        return u'{0}'.format(self.nombre)

    def __str__(self):
        return self.nombre


class Trabajador(models.Model):
    nombre = models.CharField(max_length=1000)
    apellidos = models.CharField(max_length=1000)
    aniosExperiencia = models.IntegerField()
    tiposDeServicio = models.ForeignKey(TiposDeServicio, on_delete=models.CASCADE, null=True)
    telefono = models.CharField(max_length=1000)
    correo = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='photos', null=True, blank=True)
    usuarioId = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Comentario(models.Model):
    texto = models.CharField(max_length=1000)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, null=True)
    correo = models.CharField(max_length=1000)