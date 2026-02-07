from django.urls import path
from .views import BibliotecaView

urlpatterns = [
    path('minha-biblioteca/', BibliotecaView.as_view(), name='minha-biblioteca'),
]