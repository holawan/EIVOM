from django.conf import settings
from django.db import models

class Genre(models.Model):
    #장르
    name = models.CharField(max_length=8)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_genres',blank=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    #제목 
    title = models.CharField(max_length=100)
    #원제목
    original_title = models.CharField(max_length=100)
    #영화포스터
    poster_path = models.CharField(max_length=200,null=True)
    #영화배경
    backdrop_path = models.CharField(max_length=200,null=True)
    #개요S
    overview = models.TextField()
    #개봉일
    release_date = models.DateField()
    #평점 투표수
    vote_count = models.IntegerField()
    #평점평균
    vote_average = models.FloatField()
    #인기도
    popularity = models.FloatField()
    #상영시간
    runtime = models.IntegerField(null=True)
    #한줄소개
    tagline = models.CharField(max_length=300,null=True)
    #배우
    actor_id = models.JSONField(null=True)
    actors = models.JSONField(null=True)
    actors_path = models.JSONField(null=True)
    #조회수
    view_count = models.IntegerField(default=0)
    #장르참조
    genres = models.ManyToManyField(Genre,related_name='movie_genres')
    director = models.TextField()
    #영화를 좋아하는 유저
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movies',blank=True)
    cluster=  models.IntegerField(default=0)
    def __str__(self) :
        return self.title
        
# class Actor(models.Model) :
#     name = models.CharField(max_length=20)
#     movies = models.ManyToManyField(Movie, related_name='actors',blank=True)
#     known_name = models.CharField(max_length=20)
#     def __str__(self) :
#         return self.name

class Review(models.Model) :
    #리뷰작성자
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reviews')
   #리뷰를 작성하려는 영화
   movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reviews')
   #리뷰내용
   content = models.CharField(max_length=100)
   #평점
   rate = models.IntegerField()
   #작성시간
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   #리뷰를 좋아하는 유저
   like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_reviews',blank=True)

   def __str__(self) :
       return self.content
