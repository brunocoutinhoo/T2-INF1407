from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from ..models import Barraca, Feira, Usuario, Produto
from projeto.forms.forms_barraca import BarracaForm


def lista_barracas(request, feira_id):

    barracas = Barraca.objects.filter(feira = feira_id).all()
    feira_atual = Feira.objects.filter(feira_id = feira_id).first()

    context = {
        'barracas': barracas,
        'feira_id': feira_id,
        'feira_atual': feira_atual
    }

    return render(request, "barracas/lista_barracas.html", context)


@login_required
@permission_required('project.add_barraca')
def criar_barraca(request, feira_id):

    feira_atual = Feira.objects.filter(feira_id = feira_id).first()
    current_user = request.user

    if request.method == 'POST':
        form = BarracaForm(request.POST)
        if form.is_valid():
            barraca = Barraca(
                feira = feira_atual,
                nome_barraca = form.cleaned_data['nome_barraca'],
                responsavel = current_user,
                telefone_responsavel = form.cleaned_data['telefone_responsavel'],
                numero_barraca = form.cleaned_data['numero_barraca'],
                descricao = form.cleaned_data['descricao']
            )
        try:
            barraca.save()
            messages.add_message(request, messages.INFO, _('Barraca criada com sucesso!\n'))
            return redirect(reverse('lista_barracas', args=[feira_id]))
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, _("Não foi possível criar a barraca"))

    else:
        form = BarracaForm()

    context = {
        'form': form,
        'feira_id': feira_id
    }

    return render(request, "barracas/criar_barraca.html", context)


@login_required
@permission_required('projeto.change_barraca')
def editar_barraca(request, barraca_id):
    
    barraca = get_object_or_404(Barraca, barraca_id=barraca_id)

    if request.method == 'POST':
        form = BarracaForm(request.POST, instance=barraca)
        if form.is_valid():
            barraca = form.save()
            barraca.save()
            messages.add_message(request, messages.INFO, _('barraca editada com sucesso!\n'))

            return redirect(reverse('lista_barracas'))

    form = BarracaForm(instance=barraca)

    context = {
        'form': form,
        'barraca_id': barraca_id
    }
    return render(request, 'barracas/editar_barraca.html', context)

@login_required
@permission_required('projeto.delete_barraca')
def deletar_barraca(request, barraca_id):

    barraca = get_object_or_404(Barraca, barraca_id=barraca_id)
    barraca.delete()
    messages.add_message(request, messages.INFO, _('Barraca deletada com sucesso!\n'))

    return redirect(reverse('lista_barracas'))


def visualizar_barraca(request, barraca_id):

    barraca = get_object_or_404(Barraca, barraca_id=barraca_id)
    produtos = Produto.objects.filter(barraca=barraca_id)

    context = {
        'barraca': barraca,
        'produtos': produtos,
    }

    return render(request, "barracas/visualizar_barraca.html", context)

@login_required
@permission_required('projeto.change_barraca')
def minhas_barracas(request, responsavel_id):
    
    barracas = Barraca.objects.filter(responsavel = responsavel_id).all()
    responsavel_barracas = Usuario.objects.filter(id = responsavel_id).first()

    context = {
        'barracas': barracas,
        'responsavel_barracas': responsavel_barracas
    }

    return render(request, "barracas/minhas_barracas.html", context)