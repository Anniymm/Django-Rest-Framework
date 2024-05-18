from rest_framework import generics
from rest_framework.response import Response
from django.urls import reverse
from .models import External
from .serializers import ExternalSerializer
import requests
import os


class CreateExternal(generics.ListCreateAPIView):
    queryset = External.objects.all()
    serializer_class = ExternalSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        city_name = instance.city.replace(' ', '+') # spaceiani city-s saxelistvis
        weather_url = self.request.build_absolute_uri(reverse('create_external')) + f'?city={city_name}'  #sruli url rom city-s amogheba shevdzlo da gare api-stvis gadawodeba 

        api_key = os.getenv('OPENWEATHER_API_KEY', '4ebc12f2c2438fdb9cf3b6b7a92b6586')
        weather_api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        response = requests.get(weather_api_url)  # davabrunot weather openweathermap-dan
        
        if response.status_code == 200:
            data_into_json = response.json()
            instance.weather_url = weather_api_url  
            instance.temperature = data_into_json['main']['temp']
            instance.temp_min = data_into_json['main']['temp_min']
            instance.temp_max = data_into_json['main']['temp_max']
            instance.humidity = data_into_json['main']['humidity']
            instance.description = data_into_json['weather'][0]['description']
            instance.wind_speed = data_into_json['wind']['speed']              
            instance.save() #shevinaxot bazashi yvelaferi
        # else:
        #     return Response({'city': 'sth went wrong'}) ar mushaobs
        return instance #davabrunot yvela informacia rasac bazashi shevinaxavt

    def create(self, request): #shevqmnat axali serialaizeri shemosuli informaciistvis, anu rac perform_create shemova 
        serializer = self.get_serializer(data=request.data) #get_serializer  shemosuli infostvis
        serializer.is_valid(raise_exception=True) #amit validurs vxdit serializer-is dros mighebul informacias 
        instance = self.perform_create(serializer) #aq vinaxavt perform_create-dan wamoghebul da ukve damushavebul informacias 

        queryset = self.get_queryset() #aq davabrunebt yvelafers monacemta bazidan
        all_data_serializer = self.get_serializer(queryset, many=True)  #serialaizerit ,,davamushavebt''
        return Response(ExternalSerializer(instance).data) 
    




























