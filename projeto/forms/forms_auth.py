from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.validators import RegexValidator
from projeto.models import Usuario


def valida_cpf(cpf):
    """
    função que determina se um cpf é valido (apenas números)
    algoritmo retirado de https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/

    """

    # Inicialização dos resultados para cada rodada de cálculos do algoritmo
    first_val = 0
    second_val = 0

    # Lista de cpf triviais que devem ser considerados inválidos, apesar de serem validados pelo algoritmo
    invalid_cpf = ['00000000000',
                   '11111111111',
                   '22222222222',
                   '33333333333',
                   '44444444444',
                   '55555555555',
                   '66666666666',
                   '77777777777',
                   '88888888888',
                   '99999999999']

    # Se o cpf passado for um dos considerados inválidos ou não tiver o tamanho exato, a funcção retorna falso
    if (cpf in invalid_cpf) or (len(cpf) != 11) :
        return False

    # Variáveis com dígitos verificadores do cpf passado
    first_ver_dig = int(cpf[9])
    second_ver_dig = int(cpf[10])

    # Os cálculos abaixo fazem parte do algoritmo utilizado pela Receita Federal para validar um cpf
    for position, number in enumerate(cpf[:9]):
        first_val = first_val + int(number) * (10 - position)
    first_val = (first_val * 10) % 11
    if first_val == 10:
        first_val = 0

    for position, number in enumerate(cpf[:10]):
        second_val = second_val + int(number) * (11 - position)
    second_val = (second_val * 10) % 11
    if second_val == 10:
        second_val = 0

    # Se os resultados estão de acordo com os dígitos verificadores, a função retorna verdadeiro
    if (first_val == first_ver_dig) and (second_val == second_ver_dig):
        return True
    else:  # Caso contrário, o cpf é inválido e a função retorna falso
        return False

TIPO_USUARIO = (
    ('Feirante','Feirante'),
    ('Cliente','Cliente')
)

class CadastrarUsuarioForm(forms.Form):
    usuario = forms.CharField(label='Nome de Usuário', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[RegexValidator(regex=r'^[A-Za-z\d_]+$', message='Seu usuário deve conter apenas letras, números ou _.')])
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmar_senha = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    tipo_usuario = forms.ChoiceField(label='Tipo de Usuário', choices=TIPO_USUARIO, widget=forms.Select(attrs={'class': 'form-control'}))
    nome = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sobrenome = forms.CharField(label='Sobrenome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF',required=False, widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=11, max_length=11)

    def clean_cpf(self):

        cpf = self.cleaned_data['cpf']

        if not cpf.isnumeric():
            raise ValidationError(_('Erro de inserção de CPF, insira apenas números'))
        elif not(valida_cpf(cpf)):
            raise ValidationError('CPF inválido')
        else:
            return cpf

    def clean_usuario(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')

        if len(cleaned_data.get('usuario')) < 4:
            raise ValidationError(_('Seu nome de usuário deve ter pelo menos 4 caracteres.'))

        if Usuario.objects.filter(username=usuario).count() > 0:
            raise ValidationError(_('Este usuário já existe.'))

        return usuario

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if Usuario.objects.filter(email=email).count() > 0:
            raise ValidationError(_('Este email já está associado a um usuário.'))

        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('senha')
        pass2 = cleaned_data.get('confirmar_senha')

        if pass1 is not None and pass1 != pass2:
            self.add_error('confirmar_senha', 'As senhas não correspondem.')