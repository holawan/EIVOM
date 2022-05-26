from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers.crew import  CrewListSerializer, CrewSerializer, UserSerializer
from accounts.models import User
from .models import Crew

@api_view(['GET'])
def crew_list(request):
    crews = get_list_or_404(Crew)
    print(crews)
    serializer = CrewListSerializer(crews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crew_create(request) :
    user = request.user

    serializer = CrewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.add(user)
        serializer.save(crew_leader=user)

        return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','POST'])
def crew_datail_or_update_or_signup(request,crew_pk) :
    crew = get_object_or_404(Crew,pk=crew_pk)
    user = request.user
    print(crew)
    
    def crew_detail() :
        serializer = CrewSerializer(crew)
        return Response(serializer.data)
    def crew_update() :
        if request.user == crew.crew_leader :
            serializer = CrewSerializer(instance=crew,data=request.data)
            if serializer.is_valid(raise_exception=True) :
                serializer.save(crew_leader=user)
                return Response(serializer.data)
        else :
            Response(status=status.HTTP_404_NOT_FOUND)

    def crew_signup():
        if crew.crew_users.filter(pk=user.pk).exists():
            crew.crew_users.remove(user)
            serializer = CrewSerializer(crew)
            return Response(serializer.data)
        else:
            crew.crew_users.add(user)
            serializer = CrewSerializer(crew)
            return Response(serializer.data)
                
    if request.method == 'GET' :
        return crew_detail()
    elif request.method == 'PUT' :
        return crew_update()
    elif request.method == 'POST' :
        return crew_signup()



from .models import CrewArticle,CrewReview
from .serializers.article import ArticleListSerializer,ArticleSerializer 
from .serializers.comment import CommentSerializer
@api_view(['GET', 'POST'])
def article_list_or_create(request,crew_pk):
    crew = get_object_or_404(Crew,pk=crew_pk)
    def article_list():
        # comment 개수 추가
        articles = get_list_or_404(CrewArticle,crew=crew)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    def create_article():
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user,crew=crew)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return article_list()
    elif request.method == 'POST':
        return create_article()
# @api_view(['GET'])
# def test(reqeust,user_pk) :
#     user = get_object_or_404(User,pk=user_pk) 
#     return Response(UserSerializer(user).data)
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, crew_pk,article_pk):
    crew = get_object_or_404(Crew,pk=crew_pk)
    article = get_object_or_404(CrewArticle, pk=article_pk,crew=crew)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def update_article():
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_article():
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == article.user:
            return update_article()
    elif request.method == 'DELETE':
        if request.user == article.user:
            return delete_article()

@api_view(['GET','POST'])
def comment_create_or_list(request,article_pk,crew_pk) :
    def create_comment():
        user = request.user
        article = get_object_or_404(CrewArticle, pk=article_pk)
        
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=user)

            # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
            # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            # print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def comment_list():
        comments = get_list_or_404(CrewReview,article=article_pk)
        serializer = CommentSerializer(comments,many=True)
        print(serializer.data)
        return Response(serializer.data)


    if request.method == 'POST':
        return create_comment()
    elif request.method == 'GET':
        return comment_list()

@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk,crew_pk):
    article = get_object_or_404(CrewArticle, pk=article_pk)
    comment = get_object_or_404(CrewReview, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()

