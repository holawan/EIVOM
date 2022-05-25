from dataclasses import field
from rest_framework import serializers

from .models import User,Profile
from movies.models import Genre

class ProfileSerializer(serializers.ModelSerializer) :
    
    class UserSerializer(serializers.ModelSerializer) :

        class Meta : 
            model = User 
            fields = ('pk','email')
    image = serializers.ImageField()
    backdrop = serializers.ImageField()
    # gender = serializers.SerializerMethodField()
    # location1 = serializers.SerializerMethodField()
    class Meta :
        model = Profile 
        fields = '__all__'
        read_only_fields=('user',)
    
    # def get_gender(self,obj):
    #     return obj.get_gender_display()
    # def get_location1(self,obj) :
    #     return obj.get_location1_display()



class GenreListSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Genre
        fields = ('pk','name',)

class UserSerilaizer(serializers.ModelSerializer) :
    class GenreListSerializer2(serializers.ModelSerializer) :
    
        class Meta :
            model = Genre
            fields = ('pk','name',)
    like_genres = GenreListSerializer2(read_only=True,many=True)
    class Meta :
        model = User
        fields = ('pk','like_genres',)

class GenreSerializer(serializers.ModelSerializer) :

    class UserSerializer(serializers.ModelSerializer) :
        class meta :
            model = User 
            fields = ('pk',)
    user = UserSerializer(read_only=True)

    class Meta :
        model = Genre 
        fields = ('pk','user','name')
        read_only_fields = ('user')
