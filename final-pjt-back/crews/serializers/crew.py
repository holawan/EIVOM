from accounts.models import Profile
from rest_framework import serializers

from ..models import Crew

from accounts.models import User

class UserSerializer(serializers.ModelSerializer) :

    class ProfileSerilizer(serializers.ModelSerializer) :
        class Meta : 
            model = Profile
            fields = ('nickname','image')

    profile = ProfileSerilizer(read_only=True)

    class Meta : 
        model = User
        fields = ('pk','profile',)

class CrewSerializer(serializers.ModelSerializer) :
    crew_leader = UserSerializer(read_only=True)
    crew_image = serializers.ImageField()
    crew_backdrop = serializers.ImageField()
    class Meta :
        model = Crew 
        fields = '__all__'
        read_only_fields=('crew_leader',)

# Article List Read
class CrewListSerializer(serializers.ModelSerializer):

    class Meta :
        crew_image = serializers.ImageField()
        model = Crew 
        fields = ('pk','crewname','crew_image',)


    