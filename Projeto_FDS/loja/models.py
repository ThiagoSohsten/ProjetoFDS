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



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='produtos/fotos/')
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comentario = models.TextField()
    data_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação de {self.usuario.username} em {self.data_criada}"

