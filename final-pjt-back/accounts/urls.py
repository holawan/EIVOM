from accounts import views
from django.urls import path

app_name='accounts'
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# from .views import GoogleLogin
# from .views import KakaoLogin
urlpatterns = [
    # path('google/login', GoogleLogin.as_view(), name='google_login'),
    # path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
    #프로필 만들기 
    path('profile_create/',views.profile_create,name='profile_create'),
    #프로필 조회 
    path('profile/<int:user_pk>/',views.profile_datail_or_update,name='profile'),
    #장르선택 시 보여줄 리스트 
    path('genrelist/',views.genre_list),
    path('getcrew/<int:user_pk>/',views.get_crew),
    # 회원가입 시 장르선택 
    path('selectgenre/<int:genre>/',views.genre_add),
    path('jwt/', obtain_jwt_token),          # JWT 토큰 획득
    path('jwt/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('jwt/verify/', verify_jwt_token),   # JWT 토큰 확인
]