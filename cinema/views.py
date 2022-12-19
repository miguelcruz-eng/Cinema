from itertools import chain
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import Secoes
from .models import Filme
from .models import Clientes
from .models import Produtos
from .models import Ingressos
from .models import OfertasCinema
from .forms import ClientForm
from .forms import IngressoForm


def filmList(request):
    search = request.GET.get('search')

    if search:
        filmes = Filme.objects.filter(titulo__icontains = search)

    else:
        filmes = Filme.objects.all()


        #paginator = Paginator(filmes_list, 5)

        #page = request.GET.get('page')

        #filmes = paginator.get_page(page)

    return render(request, 'cinema/list.html', {'filmes': filmes})

def filmView(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'cinema/filme.html', {'filme': filme})

def secoesFilm(request,id):
    secoes = Secoes.objects.filter(filme_id_secoes = id)#, hora_inicio = timezone.now().date())   
    return render(request, 'cinema/secoes.html', {'secoes': secoes})

def clientList(request):
    clientes = Clientes.objects.all()
    return render(request, 'cliente/cliente-list.html', {'clientes': clientes})

def clientView(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    return render(request, 'user/cliente.html', {'cliente',cliente})

def novoCliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('/')

    else:
        form = ClientForm()
    return render(request, 'cliente/cliente.html',{'form':form})

def ingressoView(request, id):
    ingresso = get_object_or_404(Ingressos, pk=id)
    return render(request, 'user/ingresso.html', {'ingresso',ingresso})

def novoIngresso(request):
    if request.method == 'POST':
        form = IngressoForm(request.POST)

        if form.is_valid():
            ingresso = form.save(commit=False)
            if ingresso.tipo_tingresso == 'Criança':
                ingresso.preco_ingresso = 15
            if ingresso.tipo_tingresso == 'Adulto':
                ingresso.preco_ingresso = 30
            if ingresso.tipo_tingresso == 'Idoso':
                ingresso.preco_ingresso = 15
            if ingresso.tipo_tingresso == 'Flamenguista':
                ingresso.preco_ingresso = 0
            else:
                ingresso.preco_ingresso = 30
            ingresso.save()
            return redirect('/')

    else:
        form = IngressoForm()
    return render(request, 'cliente/ingresso.html',{'form':form})

def lunchList(request):
    lanches = Produtos.objects.all()
    return render(request, 'lanches/list.html', {'lanches': lanches})

def lunchView(request, id):
    lanche = get_object_or_404(Produtos, pk=id)
    return render(request, 'lanches/lanche.html', {'lanche': lanche})

def promoList(request):
    promos = OfertasCinema.objects.all()
    return render(request, 'cliente/promocoes.html', {'promos': promos})