from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'created_at', 'updated_at']

class AuthorMiniSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "name", "email"]

    def get_name(self, obj):
        # Prefer full name; fall back to username
        return obj.name
    
class PostSerializer(serializers.ModelSerializer):
    author = AuthorMiniSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']
        depth = 1