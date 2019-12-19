from rest_framework import serializers
from .models import Lanche
from .models import Ingrediente

class LancheSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lanche
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ingrediente
        fields = '__all__'
