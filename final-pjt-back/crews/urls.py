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
    path('<int:crew_pk>/articles/', views.article_list_or_create),
    path('<int:crew_pk>/articles/<int:article_pk>/', views.article_detail_or_update_or_delete),
    # comments
    path('<int:crew_pk>/articles/<int:article_pk>/comments/', views.comment_create_or_list),
    path('articles/<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # path('test/<int:user_pk>/',views.test),
]