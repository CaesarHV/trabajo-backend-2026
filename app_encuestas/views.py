from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais
from .serializer import PaisSerializer


# Vista para la página de bienvenida
def bienvenida(request):
    return render(request, 'bienvenida.html')


# API para gestionar países
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer