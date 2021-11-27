from django.contrib import admin
from .models import Feira, Barraca, Produto, ListaCompras, ProdutoListaCompras

# Register your models here.

admin.site.register(Feira)
admin.site.register(Barraca)
admin.site.register(Produto)
admin.site.register(ListaCompras)
admin.site.register(ProdutoListaCompras)