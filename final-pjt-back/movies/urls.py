from movies import views
from django.urls import path

app_name='movies'

urlpatterns = [
    path('<int:movie_pk>/',views.movie_deatil),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/reviews/', views.create_or_list_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_delete)
]