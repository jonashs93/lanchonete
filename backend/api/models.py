from django.db import models

# Create your models here.

class Ingrediente(models.Model):

    class Meta:

        db_table = 'ingredientes'

    nome = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2, max_digits=4)
    alias = models.CharField(max_length=100)


    def __str__(self):
        return self.nome


class Lanche(models.Model):

    class Meta:

        db_table = 'lanches'

    nome = models.CharField(max_length=200)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return self.nome
