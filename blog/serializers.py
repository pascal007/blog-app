from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'author': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
