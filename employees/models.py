from django.db import models
from core.models import Person


class Employee(Person):
    pis = models.CharField('PIS', max_length=30, null=True)
    year_contribution = models.IntegerField('Anos_de_Contribuicao', null=True)
    function = models.CharField('Cargo_na_Empresa', max_length=150)
