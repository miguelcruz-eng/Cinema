from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone

from .models import Secoes
from .models import Filme

def filmList(request):
    filmes = Filme.objects.filter()   

    #paginator = Paginator(filmes_list, 5)

    #page = request.GET.get('page')

    #filmes = paginator.get_page(page)

    return render(request, 'cinema/list.html', {'filmes': filmes})

def filmView(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'cinema/filme.html', {'filme': filme})

def secoesFilm(request,id):
    secoes = Secoes.objects.filter(filme_i_id_filme = id,
                                    d_data_secoes = timezone.now().date())
    return render(request, 'cinema/secoes.html', {'secoes': secoes})

from .models import Lanches

def lunchList(request):
    lanches = Lanches.objects.all()
    return render(request, 'lanches/list.html', {'lanches': lanches})

def lunchView(request, id):
    lanche = get_object_or_404(Lanches, pk=id)
    return render(request, 'lanches/lanche.html', {'lanche': lanche})
