from operator import contains
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
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import Review, ReviewSerializer
import random 

@api_view(['GET'])
def genre_recommend(request) :
    user = request.user 
    genres = user.like_genres.all()
    movies = list(Movie.objects.filter(genres__in=genres).order_by('-vote_count').distinct()[:20])
    if len(movies) >11 :
        movies = random.sample(movies,12) 
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def cluster_recommend(request,cluster) :
    movies = list(Movie.objects.filter(cluster=cluster).order_by('-vote_count')[:50])
    if len(movies) >11 :
        movies = random.sample(movies,12) 
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_count_recommend(request) :
    movies = list(Movie.objects.order_by('-view_count')[:20])
    if len(movies) >11 :
        movies = random.sample(movies,12) 
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def movie_deatil(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie.view_count += 1
    movie.save()

    serializer = MovieSerializer(movie)
    return Response(serializer.data)
@api_view(['GET'])
def movie_search(request, movie_title):
    movies=Movie.objects.filter(title__contains=movie_title).order_by('-vote_count')[:10]
    # movie.view_count += 1

    serializer = MovieListSerializer(movies,many=True)
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

            # ?????? serializer ??? return ??????, ?????? review ??? ???????????? ?????????.
            # ???????????? ????????? ???????????? ????????? ??????????????? review ?????? ?????? => ??????????????? ?????? ?????? return 
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
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    
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
