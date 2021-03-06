from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreListSerializer, ProfileSerializer, UserCrewSerializer, UserSerilaizer
from movies.models import Genre
from .models import Profile
from accounts.models import User
@api_view(['POST'])
def profile_create(request) :
    user = request.user
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(user=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT'])
def profile_datail_or_update(request,user_pk) :
    user = User(pk=user_pk)
    profile =get_object_or_404(Profile,user=user)
    
    def profile_detail() :
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    def profile_update() :
        if request.user == profile.user :
            serializer = ProfileSerializer(instance=profile,data=request.data)
            if serializer.is_valid(raise_exception=True) :
                serializer.save(user=user)
                return Response(serializer.data)
        else :
            Response(status=status.HTTP_404_NOT_FOUND)
                
    if request.method == 'GET' :
        return profile_detail()
    elif request.method == 'PUT' :
        return profile_update()


@api_view(['GET'])
def genre_list(request):
    # comment 개수 추가
    genres = get_list_or_404(Genre)
    serializer = GenreListSerializer(genres,many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
def genre_add(request,genre):
    genre = get_object_or_404(Genre,pk=genre) 
    user = request.user 
    if user.like_genres.filter(pk=genre.pk).exists():
        user.like_genres.remove(genre)
        serializer = UserSerilaizer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else :
        user.like_genres.add(genre)
        serializer = UserSerilaizer(user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_crew(request,user_pk):
    user = get_object_or_404(User,pk=user_pk) 
    serializer = UserCrewSerializer(user)
    return Response(serializer.data)
# from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
import requests

# from accounts.models import User

# from django.http  import JsonResponse
# class KakaoLogin(SocialLoginView):
#     def get(self, request):
#         # kakao token 받기 / 유효성 검사를 합니다.
#         token = request.headers.get('Authorization')

#         if token == None:
#             return JsonResponse({'messsage': 'INVALID_TOKEN'}, status=401)
            
#     # kakao token을 다시 kakao로 보내서 유저 정보를 받아옵니다.
#         kakao_account = requests.get('https://kapi.kakao.com/v2/user/me', \
#             headers = {'Authorization': f'Bearer {token}'}).json()

#     # 받아온 kakao 유저정보중 id가 db에 있는지 확인합니다.
#         if not User.objects.filter(kakao_id=kakao_account['id']).exists():
#             # 유저 정보가 없으면 회원가입 되도록 합니다.
#             user = User.objects.create(
#                 kakao_id = kakao_account['id'],
#                 email    = kakao_account['kakao_account']['email']
#                 )
#             user.save()
#     adapter_class = KakaoOAuth2Adapter
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter