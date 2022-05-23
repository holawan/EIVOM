from django.urls import path
from . import views
app_name='crews'

urlpatterns = [
    #크루 리스트 (메인페이지)
    path('',views.crew_list,name='crew_list'),
    #크루만들기
    path('crew_create/',views.crew_create,name='crew_create'),
    #크루 상세정보 or 크루 업데이트, 크루 가입 
    path('<int:crew_pk>/',views.crew_datail_or_update_or_signup,name='crew'),
    path('articles/<int:crew_pk>/', views.article_list_or_create),
    path('articles/<int:crew_pk>/<int:article_pk>/', views.article_detail_or_update_or_delete),
    # comments
    path('articles/<int:crew_pk>/<int:article_pk>/comments/', views.create_comment),
    path('articles/<int:crew_pk>/<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)
]