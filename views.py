# views.py
from django.shortcuts import render
from .models import Livros

def lista_livros(request):
    livros = Livros.objects.all()
    return render(request, 'livros/lista_livros.html', {'livros': livros})

def detalhes_livro(request, id):
    livro = Livros.objects.get(id=id)
    return render(request, 'livros/detalhes_livro.html', {'livro': livro})
