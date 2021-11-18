from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    unidade = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=True, null=True)