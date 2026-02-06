from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Jogo, Plataforma 

class BibliotecaJogo(models.Model):
    STATUS_CHOICES = [
        ('QUERO', 'Quero Jogar'),
        ('JOGANDO', 'Jogando'),
        ('ZERADO', 'Zerado'),
        ('ABANDONADO', 'Abandonei'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    

    plataformas = models.ManyToManyField(Plataforma, blank=True)
    # ---------------------------

    status_atual = models.CharField(max_length=20, choices=STATUS_CHOICES, default='QUERO')
    avaliacao = models.IntegerField(null=True, blank=True)
    review = models.TextField(blank=True)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'jogo')

    def __str__(self):
        return f"{self.usuario.username} - {self.jogo.titulo}"