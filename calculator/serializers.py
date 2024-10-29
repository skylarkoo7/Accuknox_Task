from rest_framework import serializers
from calculator.models import Calculation

class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        fields = ['operation', 'result']
