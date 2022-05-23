from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie,Review
from crews.models import Crew
# Create your views here.
from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.movie import MovieSerializer
from .serializers.review import Review, ReviewSerializer
@api_view(['GET'])
def movie_deatil(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.view_count += 1
    movie.save()

    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET','POST'])
def create_or_list_review(request,movie_pk) :
    def create_review():
        user = request.user
        movie = get_object_or_404(Movie, pk=movie_pk)
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

            # 기존 serializer 가 return 되면, 단일 review 만 응답으로 받게됨.
            # 사용자가 댓글을 입력하는 사이에 업데이트된 review 확인 불가 => 업데이트된 전체 목록 return 
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def review_list() :
        reviews = Review.objects.filter(movie_id=movie_pk)
        serializer = ReviewSerializer(reviews,many=True) 
        return Response(serializer.data)
        


    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    def update_review():
        if request.user == review.user:
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                reviews = movie.reviews.all()
                serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)

    def delete_review():
        if request.user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()

from .serializers.movie import CrewMovieListSerializer

@api_view(['POST'])
def crew_add_movie(request,movie_pk,crew_pk) :
    crew = get_object_or_404(Crew,pk=crew_pk)
    movie = get_object_or_404(Movie,pk=movie_pk)
    if crew.movies.filter(pk=movie.pk).exists():
        crew.movies.remove(movie)
        serializer = CrewMovieListSerializer(crew)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    else:
        crew.movies.add(movie)
        serializer = CrewMovieListSerializer(crew)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def crew_movie_list(request,crew_pk) :
    crew = get_object_or_404(Crew,pk=crew_pk) 
    serializer = CrewMovieListSerializer(crew)
    return Response(serializer.data)
