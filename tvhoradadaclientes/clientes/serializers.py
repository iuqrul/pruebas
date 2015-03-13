from rest_framework import serializers


class ClienteSerializer(serializers.Serializer):
    dispositivo = serializers.CharField(max_length=100)
    paquete = serializers.CharField(max_length=100)
    mac = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    baneado = serializers.BooleanField()
