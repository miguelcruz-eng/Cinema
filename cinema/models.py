from django.db import models

class Filme(models.Model):
    STATUS = {
        ('cartaz', 'Cartaz'),
        ('preestreia', 'Pre-Estreia'),
    }

    title = models.CharField(max_length=255)
    description = models.TextField()
    lancamento = models.DateField()
    foto = models.TextField()
    cartaz = models.TextField()
    tipo = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lanche(models.Model):
    STATUS = {
        ('bebida', 'Bebida'),
        ('acompanhamento', 'Acompanhamento'),
        ('refeicao', 'Refeicao'),
    }

    title = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)
    description = models.TextField()
    preco = models.FloatField()
    foto = models.TextField()
    tipo = models.CharField(
        max_length=15,
        choices=STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

