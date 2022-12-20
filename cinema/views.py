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
from .models import Tipoingresso
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

def novoIngresso(request, id):
    if request.method == 'POST':
        form = IngressoForm(request.POST)
        sec = Secoes.objects.get(id = id)
        tip1 = Tipoingresso.objects.get(id_tipoingresso = 1)
        tip2 = Tipoingresso.objects.get(id_tipoingresso = 2)
        tip3 = Tipoingresso.objects.get(id_tipoingresso = 3)
        tip4 = Tipoingresso.objects.get(id_tipoingresso = 4)

        if form.is_valid():
            ingresso = form.save(commit=False)
            if ingresso.tipo_tingresso == tip1:
                ingresso.preco_ingresso = 15
            if ingresso.tipo_tingresso == tip2:
                ingresso.preco_ingresso = 30
            if ingresso.tipo_tingresso == tip3:
                ingresso.preco_ingresso = 15
            if ingresso.tipo_tingresso == tip4:
                ingresso.preco_ingresso = 0
            
            ingresso.sessao_id_ingresso = sec
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

from .models import Pedidos
from .models import ItensPedido
from .forms import PedidoForm
from .forms import IpedidosForm

def clientView(request, id):
    pedido = get_object_or_404(Pedidos, pk=id)
    return render(request, 'user/cliente.html', {'pedido',pedido})

def novoPedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return redirect('/Ipedido/')

    else:
        form = PedidoForm()
    return render(request, 'cliente/pedido.html',{'form':form})

def ipedidoView(request, id):
    ipedido = get_object_or_404(ItensPedido, pk=id)
    return render(request, 'user/cliente.html', {'ipedido',ipedido})

def novoIpedido(request):
    if request.method == 'POST':
        form = IpedidosForm(request.POST)

        if form.is_valid():
            ipedido = form.save(commit=False)
            ipedido.save()
            return redirect('/')

    else:
        form = IpedidosForm()
    return render(request, 'cliente/ipedido.html',{'form':form})

from .models import Compras
from .forms import PromoForm

def promoView(request, id):
    pcompra = get_object_or_404(Compras, pk=id)
    return render(request, 'user/cliente.html', {'pcompra',pcompra})

def novaPromo(request, id):
    if request.method == 'POST':
        form = PromoForm(request.POST)

        if form.is_valid():
            pcompra = form.save(commit=False)
            pcompra.ingresso = 0
            pcompra.lanche = 0
            pcompra.valor_total = id
            pcompra.data_compra = timezone.now().date()
            pcompra.save()
            return redirect('/')

    else:
        form = PromoForm()
    return render(request, 'cliente/carrinho-promo.html',{'form':form})