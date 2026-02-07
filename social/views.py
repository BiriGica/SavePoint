from django.shortcuts import render
from .models import BibliotecaJogo
from .serializers import BibliotecaItemSerializer
from rest_framework import generics, permissions

# Create your views here.

# LISTA os itens e CRIA novos itens
class BibliotecaView(generics.ListCreateAPIView):
    serializer_class = BibliotecaItemSerializer
    # Apenas usuários logados podem acessar isso
    permission_classes = [permissions.IsAuthenticated]

    # filtra para mostrar APENAS os jogos do usuário logado
    def get_queryset(self):
        return BibliotecaItem.objects.filter(usuario=self.request.user)

    # quando for salvar, injeta o usuário logado automaticamente
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)