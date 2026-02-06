from django.db import models

class Plataforma(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Genero(models.Model):
    nome = models.CharField(max_length=200) 
    
    def __str__(self):
        return self.nome



class Jogo(models.Model):
    titulo = models.CharField(max_length=200)
    sinopse = models.TextField(blank=True) 
    lancamentoog = models.DateField(null=True, blank=True)
    capajogo = models.URLField(blank=True) # Link da imagem

#seria no banco de dados, mas aqui pode ser feito direto. As conexões
    plataformas = models.ManyToManyField(Plataforma)
    generos = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo