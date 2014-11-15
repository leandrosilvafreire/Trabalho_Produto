from django.shortcuts import render
from produto.forms import ProdutoForm

def index(request):
    form = ProdutoForm()
    return render(request, 'index.html',{'form':form})

def validar(request):
