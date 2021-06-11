from .models import Categoria, Empresa, Estado, Hero, Municipio
from django.contrib import admin

# Register your models here.
admin.site.register(Hero)
admin.site.register(Estado)
admin.site.register(Categoria)
admin.site.register(Municipio)
admin.site.register(Empresa)
