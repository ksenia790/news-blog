from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import Post


class NewsListSerializer(ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
            