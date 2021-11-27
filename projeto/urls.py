from django.urls import path
from projeto.views.views_feira import lista_feiras, criar_feira, editar_feira, deletar_feira
from projeto.views.views_auth import cadastro_usuario
from projeto.views.views_home import index

urlpatterns = [
    path('', index, name='index'),
    path('feira/lista', lista_feiras, name='lista_feiras'),
    path('feira/criar', criar_feira, name='criar_feira'),
    path('feira/editar/<int:feira_id>', editar_feira, name='editar_feira'),
    path('feira/deletar/<int:feira_id>', deletar_feira, name='deletar_feira'),
    path('auth/cadastro', cadastro_usuario, name='cadastro_usuario')
]
