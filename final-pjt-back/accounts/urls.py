from accounts import views
from django.urls import path

app_name='accounts'

urlpatterns = [
    path('google/login', views.google_login, name='google_login'),
    path('google/login/callback/', views.google_callback,  name='google_callback'),  
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/login/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    path('profile_create/',views.profile_create,name='profile_create'),
    path('profile/<str:nickname>',views.profile_datail_or_update,name='profile'),
    path('selectgenre/',views.genre_list),
    path('selectgenre/<int:genre1>/<int:genre2>/<int:genre3>/',views.genre_add),
]