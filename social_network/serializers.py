from rest_framework import serializers
from .models import User, Post, Like, Activity


class PostSerializer(serializers.ModelSerializer):
    """Create and update new post"""

    class Meta:
        model = Post
        fields = ['owner', 'created', 'title', 'content']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Post.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']