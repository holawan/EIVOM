from django.db import models
#Django 
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser) :
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

class Profile(models.Model) :
    #Profle과 user는 1대1 관계 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    #닉네임 
    nickname = models.CharField(max_length=10)
    #프사
    image = models.TextField()
    #배경사진
    backdrop = models.TextField()
    #소개말
    introduce = models.CharField(max_length=100)
    #생년월일
    birth = models.DateField()
    #성별
    gender = models.BooleanField()
    #시/도
    location = models.CharField(max_length=4)
