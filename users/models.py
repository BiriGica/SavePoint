from django.db import models
from django.contrib.auth.models import User # Importamos o usuário padrão do Django

class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bio = models.TextField(blank=True, help_text="Gostaria de contar algo sobre você?")
    foto_perfil = models.URLField(blank=True) # Foto de perfil
    perfil_steam = models.URLField(blank=True) # Link opcional da Steam

    def __str__(self):
        return f"Perfil de {self.user.username}"