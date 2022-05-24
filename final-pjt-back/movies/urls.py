
from . import views
from django.urls import path

app_name='movies'

urlpatterns = [
    path('genre_recommend/',views.genre_recommend),
    path('cluster_recommend/<int:cluster>/',views.cluster_recommend),
    path('view_count_recommend/',views.view_count_recommend),
    #영화 디테일
    path('<int:movie_pk>/',views.movie_deatil),
    path('search/<str:movie_title>/',views.movie_search),
    #영화 좋아요 누르기 
    path('<int:movie_pk>/like/', views.like_movie),
    #리뷰 조회 및 작성
    path('<int:movie_pk>/reviews/', views.create_or_list_review),
    #리뷰 업데이트,삭제
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_delete),
    # crew에 영화 추가
    path('<int:movie_pk>/<int:crew_pk>/',views.crew_add_movie),
    #크루 영화 조회
    path('crew/<int:crew_pk>/',views.crew_movie_list),
]