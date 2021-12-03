from rest_framework import serializers
from .models import User, Post, Like, Activity


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Create and update new post"""
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['owner', 'created', 'title', 'content']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name='post-detail',
        read_only=True,
    )
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts']