from sql import Tvh


class ClienteBackend(object):
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        user = Tvh().get_cliente_by_usuario(username)
        if user:
            return user

        return None

    def get_user(self, user_id):
        user = Tvh().get_cliente(user_id)
        if user:
            return user
        return None
