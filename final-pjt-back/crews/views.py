from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  CrewListSerializer, Creweserializer
from accounts.models import User
from .models import Crew

@api_view(['GET'])
def crew_list(request):
    crews = get_list_or_404(Crew)
    print(crews)
    serializer = CrewListSerializer(crews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crew_create(request) :
    user = request.user
    serializer = Creweserializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(crew_leader=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','POST'])
def crew_datail_or_update_or_signup(request,crew_pk) :
    crew = get_object_or_404(Crew,pk=crew_pk)
    user = request.user
    print(crew)
    
    def crew_detail() :
        serializer = Creweserializer(crew)
        return Response(serializer.data)
    def crew_update() :
        if request.user == crew.crew_leader :
            serializer = Creweserializer(instance=crew,data=request.data)
            if serializer.is_valid(raise_exception=True) :
                serializer.save(crew_leader=user)
                return Response(serializer.data)
        else :
            Response(status=status.HTTP_404_NOT_FOUND)

    def crew_signup():
        if crew.crew_users.filter(pk=user.pk).exists():
            crew.crew_users.remove(user)
            serializer = Creweserializer(crew)
            return Response(serializer.data)
        else:
            crew.crew_users.add(user)
            serializer = Creweserializer(crew)
            return Response(serializer.data)
                
    if request.method == 'GET' :
        return crew_detail()
    elif request.method == 'PUT' :
        return crew_update()
    elif request.method == 'POST' :
        return crew_signup()
