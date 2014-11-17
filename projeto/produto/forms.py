from django import forms
from produto.models import Produto
#teste
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto