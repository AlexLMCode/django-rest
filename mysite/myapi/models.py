from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self) -> CharField:
        return self.name


class Estado(models.Model):
    idestado = models.IntegerField()
    estado = models.CharField(max_length=100)

    def __str__(self) -> CharField:
        return self.estado


class Categoria(models.Model):
    codigo_actividad = models.IntegerField()
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> CharField:
        return self.descripcion


class Municipio(models.Model):
    idmunicipio = models.IntegerField()
    identidad = models.IntegerField()
    nombre_municipio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> CharField:
        return self.nombre_municipio


class Empresa(models.Model):
    idempresa = models.IntegerField()
    identidad = models.IntegerField()
    idmunicipio = models.IntegerField()
    codigo_actividad = models.IntegerField()
    nombre_empresa = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitd = models.FloatField()
    calle = models.CharField(max_length=200, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=200, blank=True, null=True)
    codigo_postal = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> CharField:
        return self.nombre_empresa
