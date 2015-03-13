from django.conf.urls import patterns, include, url

from rest_framework import routers
import views



router = routers.DefaultRouter(trailing_slash=False)

router.register(r'clientes',
                views.ClientesViewSet,
                base_name='clientes')

router.register(r'facturas',
                views.FacturasViewSet,
                base_name='facturas')

router.register(r'contacto',
                views.ContactoViewSet,
                base_name='contacto')


urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
)
