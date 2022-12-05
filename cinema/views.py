from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Filme

def filmList(request):
    filmes = Filme.objects.all()
    return render(request, 'cinema/list.html', {'filmes': filmes})

def filmView(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'cinema/filme.html', {'filme': filme})
