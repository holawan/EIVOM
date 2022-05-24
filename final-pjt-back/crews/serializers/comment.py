from rest_framework import serializers
from django.contrib.auth import get_user_model

from accounts.models import Profile
from ..models import CrewReview

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
class CommentSerializer(serializers.ModelSerializer):


    user = UserSerializer(read_only=True)

    class Meta:
        model = CrewReview
        fields = ('pk', 'user', 'content', 'article',)
        read_only_fields = ('article', )
