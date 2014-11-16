from django.shortcuts import render
from produto.forms import ProdutoForm
from produto.models import Produto 

def cadastro(request):
    form = ProdutoForm()
    return render(request, 'cadastro.html',{'form':form})

def validar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST) 
        
        if form.is_valid():
            produto = Produto(**form.cleaned_data)
            produto.save()
            
            produto = Produto.objects.all()
            
            return render(request, 'validar.html',{'form':form, 'produto':produto})
        
        
        
