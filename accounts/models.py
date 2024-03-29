from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    REQUIRED_FIELDS = ['last_name']

