from rest_framework import serializers
from .models import BibliotecaJogo

class BibliotecaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibliotecaJogo
        fields = ['id', 'jogo', 'status_atual', 'avaliacao', 'review', 'plataformas']
