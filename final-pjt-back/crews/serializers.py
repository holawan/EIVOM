from rest_framework import serializers

from .models import Crew

from accounts.models import User

class Creweserializer(serializers.ModelSerializer) :
    class UserSerializer(serializers.ModelSerializer) :
        class Meta :
            model = User 
            fields = ('pk',)
    crew_leader = UserSerializer(read_only=True)
    crew_image = serializers.ImageField()
    class Meta :
        model = Crew 
        fields = '__all__'
        read_only_fields=('crew_leader',)
    

# Article List Read
class CrewListSerializer(serializers.ModelSerializer):

    class Meta :
        crew_image = serializers.ImageField()
        model = Crew 
        fields = ('crewname','crew_image')