from django.db import models

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    preco = models.CharField(max_length=5)
    quantidade = models.CharField(max_length=4)
    foto = models.ImageField(upload_to='fotos/')
    def __str__(self):
        return self.nome