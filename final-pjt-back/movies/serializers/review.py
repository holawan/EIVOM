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

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie','rate')
        read_only_fields = ('movie', )
