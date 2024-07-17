from django.shortcuts import render

from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Compra
from .serializers import CompraSerializer

class ListaCompras(generics.ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    pagination_class = LimitOffsetPagination
    pagination_class.page_size = 20
