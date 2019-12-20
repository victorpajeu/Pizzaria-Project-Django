from django.db import models
from addresses.models import Address


class Person(models.Model):
    name = models.CharField('Nome', max_length= 200, null=True)
    age = models.CharField('idade', max_length=20, null=True)
    address = models.ForeignKey(Address, verbose_name='Endereço_Pessoa', on_delete= models.CASCADE)

    class Meta:
        abstract = True
