from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Membro(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=40)
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nome', 'sobrenome']

    def __unicode__(self):
        return self.username

class Pastor(models.Model):
    membro = models.ForeignKey(Membro)
    cidade = models.CharField(max_length=40)
    estado = models.CharField(max_length=2)

    def __unicode__(self):
        return self.membro.username

class Supervisor(models.Model):
    membro = models.ForeignKey(Membro)
    pastor = models.ForeignKey(Pastor)