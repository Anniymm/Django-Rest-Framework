from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id','title','author', 'content', 'published_date'] #aq ra fieldebsac mivutitebt isini gamochndeba
        # fields = '__all__'