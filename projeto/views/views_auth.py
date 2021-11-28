from django.contrib.auth import views
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy
from django.contrib import messages
from django.contrib.auth.models import Group

from projeto.forms.forms_auth import CadastrarUsuarioForm

from projeto.models import Usuario


grupo_feirante = Group.objects.get(name='Feirante')
grupo_cliente = Group.objects.get(name='Cliente')

def cadastro_usuario(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        form = CadastrarUsuarioForm(request.POST)

        if form.is_valid():
            user = Usuario.objects.create_user(
                is_active=True,
                is_staff=False,
                is_superuser=False,

                username=form.cleaned_data['usuario'],
                password=form.cleaned_data['senha'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['nome'],
                last_name=form.cleaned_data['sobrenome'],
                cpf = form.cleaned_data['cpf']
            )
            try:
                user.save()
                if form.cleaned_data['tipo_usuario'] == 'Feirante':
                    grupo_feirante.user_set.add(user)
                if form.cleaned_data['tipo_usuario'] == 'Cliente':
                    grupo_cliente.user_set.add(user)

            except Exception as e:
                print(e)
                messages.add_message(request, messages.ERROR, gettext_lazy("Não foi possível criar o usuário"))
                pass
    else:
        form = CadastrarUsuarioForm()

    context = {
        'form': form
    }

    return render(request, 'auth/cadastro.html', context)