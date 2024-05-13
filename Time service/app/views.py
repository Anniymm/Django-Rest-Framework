from django.shortcuts import render, redirect
from .models import GetTime
from datetime import datetime
from rest_framework.response import Response
from .serializers import GetTimeSerializer
from rest_framework.views import APIView, View

class IndexView(View): #view unda gadavcet imitoro view-ebze dafudznebul class-s vqmnit
    def get(self, request):
        return render(request, 'index.html')

class AddTime(APIView): #Apiviews aris Http requestebistvis da funqciebsac shesabamisi saxelebi unda davarqvat
    def post(self, request):
        current_time = datetime.now()  
        # new_record = GetTime.objects.create(current_time = current_time) #bazashi vamateb
        # serializer = GetTimeSerializer(new_record) # es gardavqmnat da amit marto imas gamoachens romelsac chavwert
        # return Response(serializer.data)
        GetTime.objects.create(current_time = current_time) #bazashi vamateb
        updated_data = GetTime.objects.all() #bazidan momaqvs yvelaferi
        serializer = GetTimeSerializer(updated_data, many = True) # es 'jsonad gardaqmnis', many=True-ti yvelas gamovachen
        return Response(serializer.data) # abrunebs monacemebs(serialaizerit damushavebuls)
    
    def get(self, request):
        # Retrieve already saved data
        saved_data = GetTime.objects.all() #mogvaqvs yvelaferi
        serializers = GetTimeSerializer(saved_data, many=True) #serialaizerit vamushavebt
        return Response(serializers.data)
    

