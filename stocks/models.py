from django.db import models


class Stock(models.Model):
    amount = models.IntegerField('Quantidade', null=True)
    unity = models.IntegerField('Unidade_de_Medida', null=True)
    registered_at = models.TimeField('Data_de_Cadastro', auto_now=True)