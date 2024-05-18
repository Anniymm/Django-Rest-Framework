from rest_framework import serializers
from .models import External

class ExternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = External
        fields = ['id', 'city', 'weather_url', 'temperature', 'temp_min', 'temp_max', 'humidity', 'description', 'wind_speed']
