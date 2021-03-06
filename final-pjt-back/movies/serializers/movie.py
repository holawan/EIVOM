from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Profile

from ..models import Genre, Movie
from .review import ReviewSerializer

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

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_path','genres','popularity')


class MovieSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer) :
        class Meta : 
            model =Genre 
            fields = ('pk','name',)
    review = ReviewSerializer(many=True, read_only=True)
    like_users = UserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    genres = GenreSerializer(many=True,read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'original_title',
        'poster_path', 'backdrop_path','overview','release_date',
        'runtime','tagline','actor_id','actors','actors_path','vote_average',
        'director','view_count','genres','review', 'like_users','like_user_count',)

from crews.models import Crew
# Article List Read
class CrewMovieListSerializer(serializers.ModelSerializer):

    class Meta :
        model = Crew 
        fields = ('pk','crewname','movies',)