from rest_framework import serializers
from .models import MeasurementItem


class MeasurementItemSerializer(serializers.ModelSerializer):
    temperature = serializers.DecimalField(max_digits=12, decimal_places=2)
    humidity = serializers.DecimalField(max_digits=12, decimal_places=2)
    brightness = serializers.DecimalField(max_digits=12, decimal_places=2)
    atmosphericPressure = serializers.DecimalField(max_digits=12, decimal_places=2)

    #timestamp = serializers.DateTimeField()

    class Meta:
        model = MeasurementItem
        fields = ('__all__')
