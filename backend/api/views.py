from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Lanche
from .serializers import LancheSerializer
from .models import Ingrediente
from .serializers import IngredienteSerializer

class LancheList(generics.ListCreateAPIView):

    queryset = Lanche.objects.all()
    serializer_class = LancheSerializer

class IngredienteList(generics.ListCreateAPIView):

    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
