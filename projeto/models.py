from django.db import models
from django.contrib.postgres.fields import ArrayField

TIPO_UF = (
    ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'),
    ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'),
    ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),
    ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'),
    ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'),
    ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),
    ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')
)


class Feira(models.Model):
    feira_id = models.AutoField(primary_key=True)
    nome_feira = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    endereco_cep = models.CharField(max_length=8)
    endereco_uf = models.CharField(max_length=2, choices=TIPO_UF)
    endereco_cidade = models.CharField(max_length=100)
    endereco_bairro = models.CharField(max_length=50)
    endereco_logradouro = models.CharField(max_length=50)
    endereco_complemento = models.CharField(max_length=50, blank=True, null=True)
    dia_semana = models.CharField(max_length=100)


class Barraca(models.Model):
    barraca_id = models.AutoField(primary_key=True)
    feira = models.ForeignKey('Feira', on_delete=models.CASCADE,db_column='fk_feira_id', related_name='barraca_feira_fk')
    nome_barraca = models.CharField(max_length=100, blank=True, null=True)
    responsavel = models.ForeignKey('auth.User',on_delete=models.CASCADE, db_column='fk_responsavel_id', related_name='barraca_responsavel_fk')
    telefone_responsavel = models.CharField(max_length=20, blank=True, null=True)
    numero_barraca = models.CharField(max_length=5, blank=True, null=True)
    descricao = models.CharField(max_length=200, blank=True, null=True)


class Produto(models.Model):
    produto_id = models.AutoField(primary_key=True)
    barraca = models.ForeignKey('Barraca',on_delete=models.CASCADE, db_column='fk_barraca_id', related_name='produto_barraca_fk')
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    unidade = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=True, null=True)


class ListaCompras(models.Model):
    lista_id = models.AutoField(primary_key=True)
    responsavel = models.ForeignKey('auth.User',on_delete=models.CASCADE, db_column='fk_responsavel_id', related_name='lista_responsavel_fk')


class ProdutoListaCompras(models.Model):
    produtolista_id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, db_column='fk_produto_id', related_name='produtolista_produto_fk')
    lista_compras = models.ForeignKey(ListaCompras, on_delete=models.CASCADE, db_column='fk_lista_id', related_name='produtolista_lista_fk')
