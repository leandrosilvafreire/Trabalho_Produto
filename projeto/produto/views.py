from django.shortcuts import render
from produto.forms import ProdutoForm

def index(request):
    form = ProdutoForm()
    return render(request, 'index.html',{'form':form})

def validar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST) 
        
        if form.is_valid():
            produto = Produto(**form.cleaned_data)
            produto.save()
        
        
        
