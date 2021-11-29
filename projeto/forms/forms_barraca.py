from django import forms
from ..models import Barraca
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


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

    def clean_telefone_responsavel(self):
        tel = self.cleaned_data['telefone_responsavel']
        validator = RegexValidator(r"^(\(\+?55\)|\+?55)?(\(0?[0-9]{2}\)|0?[0-9]{2})?\s?[0-9]{4,5}\-?[0-9]{4}$")
        try:
            validator(tel)
        except Exception as e:
            print(e)
            raise ValidationError(_('Número de telefone inválido.'))

        return tel