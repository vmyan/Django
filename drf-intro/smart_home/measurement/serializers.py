from rest_framework import serializers
from measurement.models import Sensor, Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']  # Поля для отображения измерений


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']  # Поля для создания и обновления датчиков


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)  # Вложенный сериализатор

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']  # Поля для детального отображения
