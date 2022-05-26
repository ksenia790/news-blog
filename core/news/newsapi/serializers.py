from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from news.models import Post


class PostListSerializer(ModelSerializer):
    """
        Displays info(fields) about all posts. 
    """
    class Meta:
        model = Post
        fields = '__all__'
            