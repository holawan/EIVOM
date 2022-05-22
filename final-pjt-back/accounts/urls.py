from accounts import views
from django.urls import path

app_name='accounts'
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import GoogleLogin
from .views import KakaoLogin
urlpatterns = [
    path('google/login', GoogleLogin.as_view(), name='google_login'),
    path('kakao/login/', KakaoLogin.as_view(), name='kakao_login'),
    path('profile_create/',views.profile_create,name='profile_create'),
    path('profile/<int:user_pk>',views.profile_datail_or_update,name='profile'),
    path('genrelist/',views.genre_list),
    path('selectgenre/<int:genre1>/<int:genre2>/<int:genre3>/',views.genre_add),
    path('jwt/', obtain_jwt_token),          # JWT 토큰 획득
    path('jwt/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('jwt/verify/', verify_jwt_token),   # JWT 토큰 확인
]