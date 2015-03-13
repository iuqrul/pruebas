from rest_framework import permissions


class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS and
            request.user.is_authenticated()):
            return True

        if getattr(request.user, 'is_admin', False):
            return True


class PermisosMixin(object):
    def es_representante(self, request):
        return getattr(request.user, 'is_representante', False)

    def es_cliente(self, request):
        return getattr(request.user, 'is_cliente', False)


class IsRepresentante(permissions.BasePermission):

    def has_permission(self, request, view):
        return getattr(request.user, 'is_representante', False)


class IsCliente(permissions.BasePermission):

    def has_permission(self, request, view):
        return getattr(request.user, 'is_cliente', False)


class IsPropietario(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and \
           obj == request.user:
            return True


class ClienteORepresentanteConPermisosParaCliente(
        PermisosMixin, permissions.BasePermission):

    def has_permission(self, request, view):
        if self.es_cliente(request) or self.es_representante(request):
            return True

    def has_object_permission(self, request, view, obj):
        if self.es_cliente(request):
            return obj == request.user

        if self.es_representante(request):
            return request.user.clientes.filter(pk=obj.pk).exists()
