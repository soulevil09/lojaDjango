from django import forms
from lojaApp.models import Produto

# define o formulario
class FormProduto(forms.ModelForm):
    # dados do formulario
    class Meta:
        # modelo utilizado (tabela)
        model=Produto
        # campos que devem aparecer no form
        fields = ('nome', 'preco','quantidade','foto')
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nome'}),
            'preco':forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Preço'}),
            'quantidade':forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Quantidade'})
        }
