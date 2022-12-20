from django.urls import path

from . import views 

urlpatterns = [
    path('', views.filmList, name='film-list'),
    path('filme/<int:id>', views.filmView, name="film-view"),
    path('secoes/<int:id>', views.secoesFilm, name='secoes-list'),
    path('cliente/', views.novoCliente, name='new-client'),
    path('clientes/', views.clientList, name='client-list'),
    path('ingresso/<int:id>', views.novoIngresso, name='new-ingresso'),
    path('lanches/', views.lunchList, name='lunch-list'),
    path('lanche/<int:id>', views.lunchView, name="lunch-view"),
    path('promocoes/', views.promoList, name='promo-list'),
    path('Pedido/', views.novoPedido, name='new-pedido'),
    path('Ipedido/', views.novoIpedido, name='new-ipedido'),
    path('Pcompra/<int:id>', views.novaPromo, name='new-pcompra'),
    path('deleteCliente/<int:id>', views.deleteCliente, name='delet-cliente'),
]