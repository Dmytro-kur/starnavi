from rest_framework import serializers
from .models import User, Post, Like, Activity


class PostSerializer(serializers.ModelSerializer):
    """Create and update new post"""

    class Meta:
        model = Post
        fields = ['user', 'created', 'title', 'content']
