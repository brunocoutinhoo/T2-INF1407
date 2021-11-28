from django import forms
from ..models import Barraca


class BarracaForm(forms.ModelForm):
    nome_barraca = forms.CharField(label='Nome da Barraca', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    numero_barraca = forms.CharField(label='Número da Barraca', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone_responsavel = forms.CharField(label='Telefone do Responsável', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Barraca
        exclude = ['barraca_id', 'feira', 'responsavel']
