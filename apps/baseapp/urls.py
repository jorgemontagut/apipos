# urls.py

from django.urls import path
from .views import BancoListView, BancoDetailView, BancoCreateUpdateView, BancoDeleteView

urlpatterns = [
    path('Bancos/', BancoListView.as_view(), name='BancoListView'),
    path('Bancos/<int:pk>/', BancoDetailView.as_view(), name='BancoDetailView'),
    path('Bancos/create/', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),

    path('Bancos/update/<int:pk>', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),
    path('Bancos/delete/', BancoDeleteView.as_view(), name='BancoDeleteView'),

]


