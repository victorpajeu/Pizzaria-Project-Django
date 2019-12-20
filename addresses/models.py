from django.db import models


class Address(models.Model):
    street = models.CharField('Rua', max_length= 200, null=True)
    number = models.IntegerField('Número', null=True)
    neighborhood = models.CharField('Bairro', max_length=100, null=True)
    city = models.CharField('Cidade', max_length=100, null=True)
    country = models.CharField('País', max_length=30, null=True)