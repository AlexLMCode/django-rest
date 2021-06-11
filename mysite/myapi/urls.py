from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)
router.register(r'estados', views.EstadoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'empresas', views.EmpresaViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLS for the browsable

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
