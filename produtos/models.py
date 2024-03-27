from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nome=models.TextField(max_length=255)
    idade=models.IntegerField()

class produto(models.Model):
    nome_produto=models.CharField(max_length=100)
    preco_produto=models.DecimalField(max_digits=8, decimal_places=2)
    descricao_produto=models.TextField()

