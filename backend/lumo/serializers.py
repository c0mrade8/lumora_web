from rest_framework import serializers
from .models import User, Blog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'display_name', 'is_guest', 'created_at']

class BlogSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.display_name')

    class Meta:
        model = Blog
        fields = ['id', 'author_name', 'title', 'content', 'mood', 'created_at']