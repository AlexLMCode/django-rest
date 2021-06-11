from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import CategoriaSerializer, EmpresaSerialier, EstadoSerializer, HeroSerializer, MunicipioSerializer
from .models import Categoria, Empresa, Estado, Hero, Municipio
from django.db.models import Q
# Create your views here.


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all().order_by('idestado')
    serializer_class = EstadoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('codigo_actividad')
    serializer_class = CategoriaSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    # search_fields = ['identidad']
    # filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `municipio` query parameter in the URL.
        """
        queryset = Municipio.objects.all()
        identidad = self.request.query_params.get('identidad')
        if identidad is not None:
            queryset = queryset.filter(identidad=identidad)
        return queryset


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all().order_by('nombre_empresa')
    serializer_class = EmpresaSerialier

    def get_queryset(self):
        """
         filtering against a `municipio` query parameter in the URL.
        """
        queryset = Empresa.objects.all()
        identidad = self.request.query_params.get('identidad')
        municipio = self.request.query_params.get('idmunicipio')
        tipo = self.request.query_params.get('codigo_actividad')

        if identidad is not None and municipio is not None and tipo is not None:
            # queryset = queryset.filter(identidad=identidad, idmunicipio=municipio, codigo_actividad=tipo)
            queryset = queryset.filter(identidad=identidad).filter(
                idmunicipio=municipio).filter(codigo_actividad=tipo)
            print(queryset)
        return queryset
