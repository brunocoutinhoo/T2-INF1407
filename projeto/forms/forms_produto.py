from django import forms
from ..models import Produto


class ProdutoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do Produto', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    preco_unitario = forms.DecimalField(label='Preço de uma unidade em reais')
    unidade = forms.CharField(label='Unidade', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Produto
        exclude = ['produto_id', 'barraca']
