# from django.shortcuts import render
# from .models import Movie,Review
# # Create your views here.
# from django.shortcuts import get_object_or_404,get_list_or_404
# from django.db.models import Count

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Article, Comment
# from .serializers.movie import MovieSerializer
# from .serializers.review import Review
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_deatil(request, movie_pk):
#     moive = get_object_or_404(Movie, pk=movie_pk)

#     def article_detail():
#         serializer = MovieSerializer(moive)
#         return Response(serializer.data)

#     def update_article():
#         if request.user == article.user:
#             serializer = ArticleSerializer(instance=article, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 return Response(serializer.data)

#     def delete_article():
#         if request.user == article.user:
#             article.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)