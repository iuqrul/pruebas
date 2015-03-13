import pymssql
from unidecode import unidecode
import requests
import json
from base64 import b64decode


class UserTvh(dict):
    backend = "rest"
    is_active = True
    is_cliente = True

    def is_authenticated(self):
        return True

    @property
    def pk(self,):
        return self.get('codigo', None)

    def save(self, *args, **kwargs):
        pass

    def __unicode__(self):
        return self.get('nombre')


class Tvh(object):
    server = '192.168.200.38'
    user = 'sa'
    password = 'p@ssw0rd'
    database = 'tvh'

    goev = "http://192.168.200.38:8080/datasnap/rest/Tdocumentos/documentos/"
    goev_key = "TlYBKUZMjOabjShJeQKXflKeZNKGhGfWHhTnfGFI"

    tabla_clientes = 'ITT_PORTALCLIENTES'
    tabla_facturas = 'ITT_PORTALFACTURAS'
    tabla_facturas_lineas = 'ITT_PORTALLINEAS'
    tabla_consumos = 'ITT_PORTALCONSUMOS'

    def __init__(self):
        self.conn = pymssql.connect(self.server,
                                    self.user,
                                    self.password,
                                    self.database,
                                    port=1433)

        self.get_cursor().execute("SET LANGUAGE 'spanish'")

    def get_cursor(self):
        return self.conn.cursor(as_dict=True)

    def get_clientes(self):
        cursor = self.get_cursor()
        cursor.execute("select TOP 20 * FROM %s" % self.tabla_clientes)
        return self.transform(cursor.fetchall())

    def get_cliente(self, pk=None):
        cursor = self.get_cursor()
        cursor.execute("select * FROM %s WHERE codigo='%s'" %
                       (self.tabla_clientes, pk))
        return UserTvh(self.transform_item(cursor.fetchone()))

    def get_cliente_by_usuario(self, usuario=None):
        cursor = self.get_cursor()
        cursor.execute("select * FROM %s WHERE usuario='%s'" %
                       (self.tabla_clientes, usuario))
        return UserTvh(self.transform_item(cursor.fetchone()))

    def get_facturas_de_cliente(self, pk=None):
        cursor = self.get_cursor()
        cursor.execute(
            "select * FROM %s WHERE codcli='%s' ORDER by Ejercicio" % (self.tabla_facturas, pk))
        return cursor.fetchall()

    def es_factura_de_cliente(self, pk=None, codcli=None):
        cursor = self.get_cursor()
        cursor.execute("select * FROM %s WHERE codcli='%s' and IdFacv='%s'" %
                       (self.tabla_facturas, codcli, pk))
        return cursor.fetchall()

    def get_factura(self, pk=None):
        cursor = self.get_cursor()
        cursor.execute("select * FROM %s WHERE idfacv=%s" %
                       (self.tabla_facturas, pk))
        return cursor.fetchall()

    def get_lineas_de_factura(self, pk=None):
        cursor = self.get_cursor()
        cursor.execute("select * FROM %s where idfacv=%s" %
                       (self.tabla_facturas_lineas, pk))
        return cursor.fetchall()

    def get_consumos_de_cliente(self, codcli=None):
        cursor = self.get_cursor()
        cursor.execute(
            "select TOP 98 * FROM %s WHERE idfacv is Null order by Fecha desc, Hora desc" %
            (self.tabla_consumos))

#        cursor.execute(
#            "select * FROM %s WHERE idfacv is Null and codcli='%s' order by Fecha desc, Hora desc" %
            #            (self.tabla_consumos, codcli))
        return cursor.fetchall()

    def transform_item(self, data):
        if data:
            return {unidecode(k).lower(): unidecode(v) for k, v in data.iteritems()}

    def transform(self, data):
        return [self.transform_item(item) for item in data]

    def get_pdf_de_factura(self, pk):
        url = "%s%s" % (self.goev, pk)
        params = {
            'key': self.goev_key,
            'tipo': 4,
            'pdf': True,
            'tipomodelo': 'LSTIMPRFACV',
            'modelo': 'LSTIMPRFACV.000'
        }
        try:
            r = requests.get(url, params=params)
            response = json.loads(r.content.replace('\r\n', '').decode('cp1251').encode('utf-8'))
            archivob64 = response['ArchivoImpreso']
            return b64decode(archivob64)
        except:
            raise Exception(r.json()['error'])
