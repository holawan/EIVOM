from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import CrewArticle
from .comment import CommentSerializer

User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = CrewArticle
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_users')

from .crew import Creweserializer
# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)
    crew = Creweserializer(read_only=True)
    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)

    class Meta:
        model = CrewArticle
        fields = ('pk', 'user', 'title', 'crew',)
