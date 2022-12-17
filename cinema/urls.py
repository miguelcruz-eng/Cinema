from django.urls import path

from . import views 

urlpatterns = [
    path('', views.filmList, name='film-list'),
    path('filme/<int:id>', views.filmView, name="film-view"),
    path('secoes/<int:id>', views.secoesFilm, name='secoes-list'),
    path('cliente/', views.novoCliente, name='new-client'),
    path('lanches/', views.lunchList, name='lunch-list'),
    path('lanche/<int:id>', views.lunchView, name="lunch-view"),
]