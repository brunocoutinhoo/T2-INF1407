from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from ..models import Feira
from projeto.forms.forms_feira import FeiraForm


def lista_feiras(request):

    feiras = Feira.objects.all()

    context = {
        "feiras": feiras
    }

    return render(request, "feiras/lista_feiras.html", context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def criar_feira(request):

    if request.method == 'POST':
        form = FeiraForm(request.POST)
        if form.is_valid():
            feira = form.save()
            feira.save()
            form = FeiraForm()
            messages.add_message(request, messages.INFO, _('Feira criada com sucesso!\n'))

            return redirect(reverse('lista_feiras'))

    else:
        form = FeiraForm()

    context = {
        'form': form
    }

    return render(request, "feiras/criar_feira.html", context)



@login_required
@user_passes_test(lambda u: u.is_superuser)
def editar_feira(request, feira_id):
    
    feira = get_object_or_404(Feira, feira_id=feira_id)

    if request.method == 'POST':
        form = FeiraForm(request.POST, instance=feira)
        if form.is_valid():
            feira = form.save()
            feira.save()
            messages.add_message(request, messages.INFO, _('Feira editada com sucesso!\n'))

            return redirect(reverse('lista_feiras'))

    form = FeiraForm(instance=feira)

    context = {
        'form': form,
        'feira_id': feira_id
    }
    return render(request, 'feiras/editar_feira.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def deletar_feira(request, feira_id):

    feira = get_object_or_404(Feira, feira_id=feira_id)
    feira.delete()
    messages.add_message(request, messages.INFO, _('Feira deletado com sucesso!\n'))

    return redirect(reverse('lista_feiras'))