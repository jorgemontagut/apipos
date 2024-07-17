from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Banco, Departamento, Ciudad, TipoDocumento, FormaPago, TipoCuentaBancaria
from .serializers import BancoListaSerializer, BancoDetalleSerializer, DepartamentoListaSerializer, DepartamentoDetalleSerializer, CiudadListaSerializer, CiudadDetalleSerializer, TipoDocumentoListaSerializer,TipoDocumentoDetalleSerializer, FormaPagoListaSerializer, FormaPagoDetalleSerializer, TipoCuentaBancariaListaSerializer, TipoCuentaBancariaDetalleSerializer

class BaseListView (generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    pagination_class.page_size = 20

class BancoListView(BaseListView):
    queryset = Banco.objects.all()
    serializer_class = BancoListaSerializer

class DepartamentoListView(BaseListView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoListaSerializer
    
class CiudadListView(BaseListView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadListaSerializer
    
class TipoDocumentoListView(BaseListView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoListaSerializer
    
class FormaPagoListView(BaseListView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoListaSerializer
    
class TipoCuentaBancariaListView(BaseListView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaListaSerializer
    
########################################################################################
########  VISTAS GENÉRICAS PARA DETALLES DE CADA MODELO ################################
########################################################################################
 

class BancoDetailView(RetrieveAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoDetalleSerializer

class DepartamentosDetailView(RetrieveAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoDetalleSerializer

class CiudadDetailView(RetrieveAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadDetalleSerializer

class TipoDocumentoDetailView(RetrieveAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoDetalleSerializer


class FormaPagoDetailView(RetrieveAPIView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoDetalleSerializer


class TipoCuentaBancariaDetailView(RetrieveAPIView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA CREAR O ACTUALIZAR CADA MODELO ################################
########################################################################################


class BaseCreateUpdateView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):

    partial = True

    def perform_create(self, serializer):
        # Asignar el valor del campo 'updater' antes de guardar la instancia
        serializer.save(updater='Usuario')

    def perform_update(self, serializer):
        # Obtener la instancia del objeto Banco a actualizar
        instance = serializer.instance
        
        # Modificar el campo que no viene en el formulario
        instance.updater = 'Usuario'
        
        # Guardar los cambios en la base de datos
        instance.save()


class BancoCreateUpdateView(BaseCreateUpdateView):
    queryset = Banco.objects.all()
    serializer_class = BancoDetalleSerializer

class DepartamentoCreateUpdateView(BaseCreateUpdateView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoDetalleSerializer

class CiudadCreateUpdateView(BaseCreateUpdateView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadDetalleSerializer

class TipoDocumentoCreateUpdateView(BaseCreateUpdateView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoDetalleSerializer

class FormaPagoCreateUpdateView(BaseCreateUpdateView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoDetalleSerializer

class TipoCuentaBancariaCreateUpdateView(BaseCreateUpdateView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA MARCAR COMO ELIMINADO CADA MODELO ################################
########################################################################################


class BaseDeleteView(APIView):
    model = None
    serializer_class = None

    def patch(self, request):
        try:
            instance_id = request.data.get('id')
            instance = self.model.objects.get(pk=instance_id)
        except self.model.DoesNotExist:
            return Response({"error": f"{self.model.__name__} no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Marcar registro como eliminado
        instance.deleter = 'Usuario'
        instance.deleted = timezone.now()
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

class BancoDeleteView(BaseDeleteView):
    model = Banco
    serializer_class = BancoDetalleSerializer

class DepartamentoDeleteView(BaseDeleteView):
    model = Departamento
    serializer_class = DepartamentoDetalleSerializer

class CiudadDeleteView(BaseListView):
    nidek = Ciudad
    serializer_class = CiudadListaSerializer
    
class TipoDocumentoDeleteView(BaseListView):
    nidek = TipoDocumento
    serializer_class = TipoDocumentoListaSerializer
    
class FormaPagoDeleteView(BaseListView):
    nidek = FormaPago
    serializer_class = FormaPagoListaSerializer
    
class TipoCuentaBancariaDeleteView(BaseListView):
    nidek = TipoCuentaBancaria
    serializer_class = TipoCuentaBancariaListaSerializer
    


