from django.urls import path
from projeto.views.views_feira import lista_feiras, criar_feira, editar_feira, deletar_feira
from projeto.views.views_barraca import lista_barracas, criar_barraca, editar_barraca, deletar_barraca, visualizar_barraca
from projeto.views.views_auth import cadastro_usuario
from projeto.views.views_home import index

urlpatterns = [
    path('', index, name='index'),
    path('feira/lista', lista_feiras, name='lista_feiras'),
    path('feira/criar', criar_feira, name='criar_feira'),
    path('feira/editar/<int:feira_id>', editar_feira, name='editar_feira'),
    path('feira/deletar/<int:feira_id>', deletar_feira, name='deletar_feira'),
    path('registration/cadastro', cadastro_usuario, name='cadastro_usuario'),
    path('barraca/lista/<int:feira_id>', lista_barracas, name='lista_barracas'),
    path('barraca/criar/<int:feira_id>', criar_barraca, name='criar_barraca'),
    path('barraca/editar/<int:barraca_id>', editar_barraca, name='editar_barraca'),
    path('barraca/deletar/<int:barraca_id>', deletar_barraca, name='deletar_barraca'),
    path('barraca/visualizar/<int:barraca_id>', visualizar_barraca, name='visualizar_barraca'),
]
