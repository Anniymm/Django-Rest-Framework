
from django.db import models

class External(models.Model):
    city = models.CharField(max_length=100)
    weather_url = models.URLField(max_length=200,  null=True)
    temperature = models.FloatField(null=True, blank=True)
    temp_min = models.FloatField(null=True, blank=True)
    temp_max = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True)
    wind_speed = models.FloatField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.city