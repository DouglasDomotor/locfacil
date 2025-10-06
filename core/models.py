from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20, unique=True)
    celular = models.CharField(max_length=15)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    ano = models.IntegerField()
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    
    def valor_estimado_venda(self):
        pass
