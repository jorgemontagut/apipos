# serializers.py

from rest_framework import serializers
from .models import Banco, Departamento, Ciudad, TipoDocumento, FormaPago, TipoCuentaBancaria

####################################################################
#lista de bancos
class BancoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
   #     fields = '__all__'
        fields = 'id', 'nombre', 'get_absolute_url'

#detalle de cada banco
class BancoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
   
        fields = 'id', 'nombre', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#######################################################################
#lista de departamentos
class DepartamentoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
   #     fields = '__all__'
        fields = 'id', 'nombre','cod_dane', 'get_absolute_url'

class DepartamentoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
   
        fields = 'id', 'nombre', 'cod_dane', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#######################################################################

#lista de ciudades
class CiudadListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
   #     fields = '__all__'
        fields = 'id', 'nombre', 'get_absolute_url'

#detalle de cada ciudad
class CiudadDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
   
        fields = 'id', 'nombre', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

#####################################################################

#lista de TiposDocumento
class TipoDocumentoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
   #     fields = '__all__'
        fields = 'id', 'nombre', 'get_absolute_url'

#detalle de cada TipoDocumento
class TipoDocumentoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
   
        fields = 'id', 'nombre', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

#####################################################################

#lista de FormasPagos
class FormaPagoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
   #     fields = '__all__'
        fields = 'id', 'nombre', 'get_absolute_url'

#detalle de cada FormaPago
class FormaPagoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
   
        fields = 'id', 'nombre', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

#####################################################################

#lista de TiposCuentaBancaria
class TipoCuentaBancariaListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuentaBancaria
   #     fields = '__all__'
        fields = 'id', 'nombre', 'get_absolute_url'

#detalle de cada TipoCuentaBancaria
class TipoCuentaBancariaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCuentaBancaria
   
        fields = 'id', 'nombre', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

#####################################################################