from django import forms
from ..models import Barraca


TIPO_UF = (
    ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'),
    ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'),
    ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),
    ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'),
    ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'),
    ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),
    ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
)

class BarracaForm(forms.ModelForm):
    nome_barraca = forms.CharField(label='Nome da Barraca', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    numero_barraca = forms.CharField(label='Número da Barraca', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone_responsavel = forms.CharField(label='Telefone do Responsável', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Barraca
        exclude = ['barraca_id', 'feira', 'responsavel']
