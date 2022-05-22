from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie
from .review import ReviewSerializer

User = get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    review = ReviewSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'user', 'title', 'original_title','poster_path', 'backdrop_path','overview','release_date','runtime','tagline','actor_id','actors','actors_path','director','view_count','genres','comments', 'like_users')