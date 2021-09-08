from django.db import models
from django.contrib.auth.models import User

class Contatos(models.Model):
    nome = models.CharField(max_length=80)
    numero = models.CharField(max_length=17)
    empresa = models.ForeignKey('Empresa', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Conta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_created=True, auto_now=True)

    
# Create your models here.
