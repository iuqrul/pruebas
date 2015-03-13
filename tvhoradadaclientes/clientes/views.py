# encoding: utf-8
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework import serializers
from .sql import Tvh
from .utils import enviar_mail_cambio_de_datos, enviar_mail_de_contacto
from django.views.generic.base import TemplateView
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseServerError


class ClientesViewSet(viewsets.GenericViewSet):

    """Usando esta api se puede acceder a los detalles de los clientes de
    la aplicación de tvhoradada.

    Cuando un cliente se identifique con sus datos sólo podrá ver en
    el listado sus propios datos.

    #### Parámetros para filtrado
    * Pendiente de implementación

    #### Parámetros de búsqueda
    * Pendiente de implementación

    # Detalles de un cliente
    **/api/v1/clientes/<pk\>**

    # Listado de facturas del cliente cliente
    Además se puede acceder a las facturas de un cliente.
    **/api/v1/clientes/<pk\>/facturas**
    """
    serializer_class = serializers.Serializer

    def list(self, request):
        if hasattr(request.user, 'is_cliente') and getattr(request.user, 'is_cliente', False):
            result = [dict(request.user)]
        else:
            result = Tvh().get_clientes()

        return Response(result)

    def retrieve(self, request, pk=None):
        if hasattr(request.user, 'is_cliente') and getattr(request.user, 'is_cliente', False):
            result = Tvh().get_facturas_de_cliente(request.user.pk)

        return Response(result)

    def create(self, request):
        enviar_mail_cambio_de_datos(request)
        return Response({'message': 'La solicitud de cambio de datos ha sido enviada'})

    @link()
    def facturas(self, request, pk=None):
        if hasattr(request.user, 'is_cliente') and getattr(request.user, 'is_cliente', False):
            result = Tvh().get_facturas_de_cliente(request.user.pk)
            return Response(result)
        return Response(status_code=403)

    @link()
    def consumos(self, request, pk=None):
        if hasattr(request.user, 'is_cliente') and getattr(request.user, 'is_cliente', False):
            result = Tvh().get_consumos_de_cliente(request.user.pk)
            return Response(result)
        return Response(status_code=403)


class FacturasViewSet(viewsets.GenericViewSet):

    """Usando esta api se puede acceder a los detalles de la facturación
    de los clientes para la aplicación de tvhoradada.

    Cuando un cliente se identifique con sus datos sólo podrá ver en
    el listado sus facturas.

    #### Parámetros para filtrado
    * Pendiente de implementación

    #### Parámetros de búsqueda
    * Pendiente de implementación

    # Detalles de la cabecera factura
    **/api/v1/facturas/<pk\>**

    # Listado de las líneas de la factura
    **/api/v1/facturas/<pk\>/lineas**

    # Listado de los consumos de esa factura
    **/api/v1/facturas/<pk\>/consumos**

    """

    def check_permisos_a_factura(self, pk):
        if hasattr(self.request.user, 'is_cliente') and getattr(self.request.user, 'is_cliente', False):
            return Tvh().es_factura_de_cliente(pk, self.request.user.get('codigo'))
        return False

    def list(self, request):
        if hasattr(request.user, 'is_cliente') and getattr(request.user, 'is_cliente', False):
            response = Tvh().get_facturas_de_cliente(
                request.user.get('codigo'))
            return Response(response)
        return Response({}, status_code=403)

    def retrieve(self, request, pk=None):
        if self.check_permisos_a_factura(pk):
            result = Tvh().get_factura(pk)
            return Response(result)
        return HttpResponseForbidden("<h1>Acceso no permitido</h1>")

    @link()
    def lineas(self, request, pk=None):
        if self.check_permisos_a_factura(pk):
            result = Tvh().get_lineas_de_factura(pk)
            return Response(result)
        return HttpResponseForbidden("<h1>Acceso no permitido</h1>")


class ContactoViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.Serializer

    def create(self, request):
        enviar_mail_de_contacto(request)
        return Response({'message': 'El mensaje ha sido enviado. Muchas gracias por contactar con nosotros'})


class DownloadPDF(TemplateView):

    def render_to_response(self, context, **response_kwargs):
        if hasattr(self.request.user, 'is_cliente') and getattr(self.request.user, 'is_cliente', False):
            if Tvh().es_factura_de_cliente(self.kwargs['pk'], self.request.user.get('codigo')):
                try:
                    return HttpResponse(Tvh().get_pdf_de_factura(self.kwargs['pk']), content_type='Application/pdf')
                except Exception as e:
                    return HttpResponseServerError("<h1>%s</h1>" % e)

        return HttpResponseForbidden("<h1>Acceso no permitido</h1>")
