# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    NICHO_CHOICES = [
        ('moda', 'Moda Praia'),
        ('esporte', 'Esportes Aquáticos'),
        # ... Adicione mais categorias conforme necessário
    ]

    nicho = models.CharField(max_length=50, choices=NICHO_CHOICES, null=True, blank=True)



# loja/models.py

from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='produtos/fotos/', blank=True, null=True)

    def __str__(self):
        return self.nome



class Avaliacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario.username} em {self.data_criada}"



class Carrinho(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
class Cartao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    numero = models.CharField(max_length=16)
    validade = models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return f'Cartão final {self.numero[-4:]} de {self.usuario.username}'
class Devolucao(models.Model):
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    data_devolucao = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado')
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Devolução de {self.pedido.usuario.username} em {self.data_devolucao}"
class Pedido(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()


