from rest_framework import serializers
from .models import GetTime

class GetTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetTime
        fields = '__all__'