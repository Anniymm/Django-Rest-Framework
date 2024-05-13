from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogChanging(generics.RetrieveUpdateDestroyAPIView): #RetrieveUpdateDestroyAPIView wvdomas gvadzlevs individualurad
    queryset = BlogPost.objects.all() #amit yvelaferi wamovighot
    serializer_class = BlogPostSerializer #aq serialaizeri unda mivutitot romelzec vmoqmedebt
    lookup_field = 'pk' #aq individualurad rom mivakitxot id-ebit. 

# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     lookup_field = 'title'  #es roca title-it mindds rom mivakitxo