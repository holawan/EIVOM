from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Review

User = get_user_model()

# CUD => validation
# R => Data serializing
class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk',)

    user = UserSerializer(read_only=True)
    # like_users = UserSerializer(read_only=True, many=True)
    like_user_count = serializers.IntegerField(source='like_users.count', read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie','created_at','rate','like_user_count')
        read_only_fields = ('movie', )
