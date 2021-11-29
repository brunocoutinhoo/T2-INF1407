from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from ..models import ListaCompras, Produto


@login_required
def adicionar_produto_lista(request, produto_id):
    produto = get_object_or_404(Produto, produto_id=produto_id)

    if ListaCompras.objects.filter(cliente=request.user, produto=produto).exists():
        messages.add_message(request, messages.INFO, _('Produto já está na sua lista!\n'))
        return redirect(reverse('visualizar_lista_compras'))

    item_lista = ListaCompras(
        cliente = request.user,
        produto = produto,
    )
    item_lista.save()
    messages.add_message(request, messages.INFO, _('Produto adicionado à sua lista!\n'))
    return redirect(reverse('visualizar_lista_compras'))

@login_required
def remover_produto_lista(request, produto_id):
    produto_lista = ListaCompras.objects.filter(cliente=request.user, produto__produto_id=produto_id).first()
    if not produto_lista:
        return HttpResponseNotFound()

    produto_lista.delete()
    messages.add_message(request, messages.INFO, _('Produto deletado com sucesso!\n'))

    return redirect(reverse('visualizar_lista_compras'))

@login_required
def visualizar_lista_compras(request):
    produtos_lista = ListaCompras.objects.filter(cliente=request.user)

    context = {
        'produtos_lista': produtos_lista
    }
    
    return render(request, 'lista_compras/visualizar_lista.html', context=context)