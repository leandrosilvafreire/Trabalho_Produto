from django.shortcuts import render
from produto.forms import ProdutoForm

def index(request):
    form = ProdutoForm()
