from django.db import models


class Product(models.Model):
    name = models.CharField('Nome', max_length=300, null=True)
    description = models.CharField('Descricao_Produto', max_length=1000, null=True)