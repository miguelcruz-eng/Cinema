from django.db import models

class Filme(models.Model):
    STATUS = {
        ('estreia', 'Estreia'),
        ('preestreia', 'Pre-Estreia'),
    }

    title = models.CharField(max_length=255)
    description = models.TextField()
    lancamento = models.CharField(max_length=255)
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
