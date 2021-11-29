from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from ..models import Produto, Barraca
from projeto.forms.forms_produto import ProdutoForm

@login_required
def adicionar_produto(request, barraca_id):

    barraca_atual = Barraca.objects.get(barraca_id=barraca_id)
    usuario_atual = request.user

    if not (barraca_atual.responsavel == usuario_atual):
        raise PermissionDenied()
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, auto_id=True)
        if form.is_valid():
            produto = Produto(
                barraca = barraca_atual,
                nome = form.cleaned_data['nome'],
                descricao = form.cleaned_data['descricao'],
                preco_unitario = form.cleaned_data['preco_unitario'],
                unidade = form.cleaned_data['unidade']
            )
        try:
            produto.save()
            messages.add_message(request, messages.INFO, _('Produto adicionado com sucesso!\n'))
            return redirect(reverse('visualizar_barraca', args=[barraca_atual]))
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, _("Não foi possível adicionar o produto"))
    else:
        if "term" in request.GET:
            qs = Produto.objects.filter(nome__istartswith=request.GET.get('term'))
            nomes = []
            for produto in qs:
                nomes.append(produto.nome)
            return JsonResponse(nomes, safe=False)
        form = ProdutoForm()

    context = {
        'form': form,
        'barraca_id': barraca_id
    }

    return render(request, "produtos/adicionar_produto.html", context)

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, produto_id=produto_id)
    if not (produto.barraca.responsavel == request.user):
        raise PermissionDenied()

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            produto = form.save()
            produto.save()
            messages.add_message(request, messages.INFO, _('Produto editado com sucesso!\n'))

            return redirect(reverse('visualizar_barraca', args=[produto.barraca]))

    form = ProdutoForm(instance=produto)

    context = {
        'form': form,
        'produto_id': produto_id
    }
    return render(request, 'produtos/editar_produtos.html', context)

@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, produto_id=produto_id)
    if not (produto.barraca.responsavel == request.user):
        raise PermissionDenied()
    
    produto.delete()
    messages.add_message(request, messages.INFO, _('Produto deletado com sucesso!\n'))

    return redirect(reverse('visualizar_barraca', args=[produto.barraca]))
    
