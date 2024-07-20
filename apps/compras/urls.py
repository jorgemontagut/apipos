# urls.py

from django.urls import path
from .views import ListaCompras

urlpatterns = [
    path('Compras/', ListaCompras.as_view(), name='lista-Compras'),
    path('', ListaCompras.as_view(), name='lista-Compras'),

]



