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


