from django.db.models import fields
from rest_framework import serializers
from .models import Categoria, Empresa, Estado, Hero, Municipio


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ('idestado', 'estado')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('codigo_actividad', 'descripcion')


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = ('idmunicipio',
                  'identidad',
                  'nombre_municipio')


class EmpresaSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = ('idempresa',
                  'identidad',
                  'idmunicipio',
                  'codigo_actividad',
                  'nombre_empresa',
                  'latitud',
                  'longitd',
                  'calle',
                  'numero',
                  'colonia',
                  'codigo_postal',
                  'ciudad',
                  'estado',
                  'descripcion')
