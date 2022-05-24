from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Profile
from ..models import Review

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
# CUD => validation
# R => Data serializing
class ReviewSerializer(serializers.ModelSerializer):



    user = UserSerializer(read_only=True)
    # like_users = UserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie','created_at','rate','like_user_count')
        read_only_fields = ('movie', )
