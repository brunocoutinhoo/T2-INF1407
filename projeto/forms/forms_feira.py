from django import forms
from ..models import Feira


TIPO_UF = (
    ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'),
    ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'),
    ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),
    ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'),
    ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'),
    ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),
    ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
)

class FeiraForm(forms.ModelForm):
    nome_feira = forms.CharField(label='Nome da Feira', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descricao = forms.CharField(label='Descrição', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}))
    endereco_cep = forms.CharField(max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_uf = forms.ChoiceField(choices=TIPO_UF, widget=forms.Select(attrs={'class': 'form-control'}), initial="RJ")
    endereco_cidade = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_bairro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_logradouro = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_complemento = forms.CharField(required=False , max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dia_semana = forms.CharField(required=False , max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Feira
        exclude = ['feira_id']