from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Profile

from ..models import Crew, CrewArticle
from .comment import CommentSerializer

User = get_user_model()
class UserSerializer(serializers.ModelSerializer) :

    class ProfileSerilizer(serializers.ModelSerializer) :
        class Meta : 
            model = Profile
            fields = ('nickname','image')

    profile = ProfileSerilizer(read_only=True)

    class Meta : 
        model = User
        fields = ('pk','profile',)

class ArticleSerializer(serializers.ModelSerializer):
    

    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = CrewArticle
        fields = ('pk', 'user', 'title', 'content', 'comments', 'like_users')

class Creweserializer(serializers.ModelSerializer) :
    class UserSerializer(serializers.ModelSerializer) :
        class Meta :
            model = User 
            fields = ('pk',)

    class Meta :
        model = Crew 
        fields = ('pk','crewname')
# Article List Read
class ArticleListSerializer(serializers.ModelSerializer):

    crew = Creweserializer(read_only=True)
    user = UserSerializer(read_only=True)
    # queryset annotate (views에서 채워줄것!)

    class Meta:
        model = CrewArticle
        fields = ('pk', 'user', 'title', 'content','crew',)
