"""apiserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
    path('crews/',include('crews.urls')),
    path('accounts/',include('dj_rest_auth.urls')),
    path('accounts/signup/',include('dj_rest_auth.registration.urls')),
    path('accounts/',include('allauth.urls')),
    path('accounts/',include('accounts.urls')),
    path('api-jwt-auth/', obtain_jwt_token),          # JWT 토큰 획득
    path('api-jwt-auth/refresh/', refresh_jwt_token), # JWT 토큰 갱신
    path('api-jwt-auth/verify/', verify_jwt_token),   # JWT 토큰 확인
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
