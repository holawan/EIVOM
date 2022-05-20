from rest_framework import serializers

from .models import User,Profile


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

