from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Membro(AbstractBaseUser):
    email = models.CharField(max_length=40, unique=True)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'sobrenome']