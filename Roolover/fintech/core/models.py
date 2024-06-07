from django.db import models

# Create your models here.
from django.db import models

class ContaMae(models.Model):
    nome = models.CharField(max_length=100)
    taxa_deposito = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome

class ContaFilha(models.Model):
    nome = models.CharField(max_length=100)
    conta_mae = models.ForeignKey(ContaMae, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    porcentagem_fixa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    cpf_validos = models.TextField(null=True, blank=True)  # Lista de CPFs válidos, armazenada como texto (JSON, CSV, etc.)

    def __str__(self):
        return self.nome

class SplitRule(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    conta_mae = models.ForeignKey(ContaMae, on_delete=models.CASCADE)
    porcentagem = models.DecimalField(max_digits=5, decimal_places=2)
    requisito_cpf = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.conta_mae.nome}"
