from django.shortcuts import get_list_or_404, redirect, render
from django.conf import settings
from accounts.models import Profile, User
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from rest_framework import status

from accounts import managers, serializers
from movies.models import Genre
# Create your views here.

# 구글 
state = getattr(settings, 'STATE')
BASE_URL = 'http://localhost:8000/'
GOOGLE_CALLBACK_URI = BASE_URL + 'accounts/google/login/callback/'
print(GOOGLE_CALLBACK_URI)

def google_login(request):
    """
    Code Request
    """
    scope = "https://www.googleapis.com/auth/userinfo.email"
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")
# 이 함수와 매핑된 url로 들어가면, client_id, redirect uri 등과 같은 정보를 url parameter로 함께 보내 리다이렉트한다. 
# 그러면 구글 로그인 창이 뜨고, 알맞은 아이디, 비밀번호로 진행하면 Callback URI로 Code값이 들어가게 된다.

def google_callback(request):
    client_id = getattr(settings, "SOCIAL_AUTH_GOOGLE_CLIENT_ID")
    client_secret = getattr(settings, "SOCIAL_AUTH_GOOGLE_SECRET")
    code = request.GET.get('code')
    """
    Access Token Request
    """
    #구글에 Access Token 요청
    token_req = requests.post(
        f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get('access_token')
    # Google API Server에 응답받은 Code, client_secret, state와 같은 url parameter를 함께 Post 요청을 보낸다. 
    # 문제없이 성공하면, access_token을 가져올 수 있다.
    """
    Email Request
    """
    #Access Token으로 Email 값을 Google에게 요청
    email_req = requests.get(
        f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
    email_req_status = email_req.status_code
    if email_req_status != 200:
        return JsonResponse({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)
    email_req_json = email_req.json()
    email = email_req_json.get('email')
    #응답받은 Access Token을 로그인된 사용자의 Email을 응답받기 위해 url parameter에 포함하여 요청 
    # - Access Token이 틀렸거나, 에러 발생으로 200 OK 코드를 응답받지 못하면 400으로 Response
    """
    Signup or Signin Request
    """
    #전달받은 Email, Access Token, Code를 바탕으로 회원가입/로그인 진행

    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 google이 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}accounts/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}accounts/google/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

    ### 
    ###
    #1. 전달받은 email과 동일한 Email이 있는지 찾아본다.
    #2-1. 만약 있다면?
    #    - FK로 연결되어있는 socialaccount 테이블에서 이메일의 유저가 있는지 체크
    #    - 없으면 일반 계정이므로, 에러 메세지와 함께 400 리턴
    #    - 있지만 다른 Provider로 가입되어 있으면 에러 메세지와 함께 400 리턴
    #    - 위 두개에 걸리지 않으면 로그인 진행, 해당 유저의 JWT 발급, 그러나 도중에          
    #        예기치 못한 오류가 발생하면 에러 메세지와 함께 오류 Status 응답
    #2-2. 없다면 (신규 유저이면)
    #    - 회원가입 진행 및 해당 유저의 JWT 발급
    #    - 그러나 도중에 예기치 못한 오류가 발생하면 에러 메세지와 함께 오류 Status응답

class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


BASE_URL2=  'http://127.0.0.1:8000/'
KAKAO_CALLBACK_URI = BASE_URL2 + 'accounts/kakao/login/callback/'
print(KAKAO_CALLBACK_URI)
def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )
def kakao_callback(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    code = request.GET.get("code")
    redirect_uri = KAKAO_CALLBACK_URI
    """
    Access Token Request
    """
    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")
    """
    Email Request
    """
    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    kakao_account = profile_json.get('kakao_account')
    """
    kakao_account에서 이메일 외에
    카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
    print(kakao_account) 참고
    """
    # print()
    email = kakao_account.get('email')
    """
    Signup or Signin Request
    """
    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        if social_user.provider != 'kakao':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL2}accounts/api/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        print('accept_json:',accept_json)
        accept_json.pop('user', None)
        print('awfleaweofiowaejfo')
        return JsonResponse(accept_json)
    except User.DoesNotExist:
        # 기존에 가입된 유저가 없으면 새로 가입
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL2}accounts/kakao/login/finish/", data=data)
        print(f'{BASE_URL2}accounts/kakao/login/finish/')
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)

class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    callback_url = KAKAO_CALLBACK_URI
    client_class = OAuth2Client

from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreListSerializer, ProfileSerializer

@api_view(['POST'])
def profile_create(request) :
    user = request.user
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(user=user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT'])
def profile_datail_or_update(request,nickname) :
    user = request.user
    profile =get_object_or_404(Profile,nickname=nickname)
    
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
def genre_add(request,genre1,genre2,genre3):
    genre1 = get_object_or_404(Genre,pk=genre1) 
    genre2 = get_object_or_404(Genre,pk=genre2) 
    genre3 = get_object_or_404(Genre,pk=genre3) 
    user = request.user 
    user.like_genres.add(genre1)
    user.like_genres.add(genre2)
    user.like_genres.add(genre3)
    return Response(status=status.HTTP_201_CREATED)

    
