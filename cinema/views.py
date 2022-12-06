from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages

from .models import Filme

def filmList(request):
    filmes_list = Filme.objects.all()

    paginator = Paginator(filmes_list, 5)

    page = request.GET.get('page')

    filmes = paginator.get_page(page)

    return render(request, 'cinema/list.html', {'filmes': filmes})

def filmView(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'cinema/filme.html', {'filme': filme})


from .models import Lanche

def lunchList(request):
    lanches = Lanche.objects.all()
    return render(request, 'lanches/list.html', {'lanches': lanches})

def lunchView(request, id):
    lanche = get_object_or_404(Lanche, pk=id)
    return render(request, 'lanches/lanche.html', {'lanche': lanche})
