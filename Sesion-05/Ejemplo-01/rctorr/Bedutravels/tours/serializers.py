from rest_framework import serializers

from .models import Zona, Tour


class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Tour """
    class Meta:
        # Se define sobre que modelo actúa
        model = Tour
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'slug', 'operador', 'tipoDeTour',
         'descripcion', 'img', 'pais', 'zonaSalida', 'zonaLlegada')


class ZonaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para atender las conversiones para Zona """

    # Se define la relación de una zona y sus tours realizados
    tours = TourSerializer(many=True, read_only=True)

    class Meta:
        # Se define sobre que modelo actua
        model = Zona
        # Se definen los campos a incluir
        fields = ('id', 'nombre', 'descripcion', 'latitud',
        	'longitud', 'tours', 'tours_llegada', 'tours_salida')


