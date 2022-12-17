from itertools import chain
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone

from .models import Secoes
from .models import Filme
from .models import Clientes
from .forms import ClientForm

def filmList(request):
    search = request.GET.get('search')

    if search:
        filmes = Filme.objects.filter(s_titulo_filme__icontains = search)

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
    secoes = Secoes.objects.filter(filme_i_id_filme = id,d_data_secoes = timezone.now().date())
    
    return render(request, 'cinema/secoes.html', {'secoes': secoes})

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

from .models import Produtos

def lunchList(request):
    lanches = Produtos.objects.all()
    return render(request, 'lanches/list.html', {'lanches': lanches})

def lunchView(request, id):
    lanche = get_object_or_404(Produtos, pk=id)
    return render(request, 'lanches/lanche.html', {'lanche': lanche})
