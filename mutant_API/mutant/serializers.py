from dataclasses import field
from rest_framework import serializers
from .models import Mutant

class MutantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mutant
        fields = '__all__'
      