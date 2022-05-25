from email.policy import default
from django.db import models
#Django 
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from movies.models import Genre
from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser) :
    username = None
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()
    spouse_name = models.CharField(blank=True, max_length=100)

    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self) :
        return self.email


class Profile(models.Model) :
    #Profle과 user는 1대1 관계 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    #닉네임 
    nickname = models.CharField(max_length=10,unique=True,null=True,blank=True,)
    #프사
    image = ProcessedImageField(
    null=True,blank=True,
    upload_to='thumbnails/user/profile/',
    # processors=[Thumbnail(300, 300)],
    format='JPEG',
    options={'quality': 100},
    default='media/user/프로필기본.png')
    #배경사진
    backdrop = ProcessedImageField(
    null=True,blank=True,
    upload_to='thumbnails/user/backdrop/',
    # processors=[Thumbnail(1200, 800)],
    format='JPEG',
    options={'quality': 100},
    default='media/user/프로필배경기본.png'
    )
    #소개말
    introduce = models.CharField(max_length=100,null=True,blank=True)
    #생년월일
    birth = models.DateField(null=True,blank=True,)
    #성별
    GENDER_CHOICES = (
        ('남성','남성'),
        ('여성','여성')
    )
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,null=True,blank=True)
    #도/특별시/광역시
    LOCATION_COHICES = (
        ('서울특별시','서울특별시'),
        ('부산광역시','부산광역시'),
        ('대구광역시','대구광역시'),
        ('인천광역시','인천광역시'),
        ('광주광역시','광주광역시'),
        ('대전광역시','대전광역시'),
        ('울산광역시','울산광역시'),
        ('세종특별자치시','세종특별자치시'),
        ('경기도','경기도'),
        ('강원도','강원도'),
        ('충청북도','충청북도'),
        ('충청남도','충청남도'),
        ('전라북도','전라북도'),
        ('전라남도','전라남도'),
        ('경상북도','경상북도'),
        ('경상남도','경상남도'),
        ('제주특별자치도','제주특별자치도'),

    )
    location1 = models.CharField(max_length=10,choices=LOCATION_COHICES,null=True,blank=True)
    #시/군/구
    location2 = models.CharField(max_length=5,null=True,blank=True)
    def __str__(self) :
        return self.nickname

from django.conf import settings
from django.db import models





from django.contrib.auth.signals import user_logged_in

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    session_key = models.CharField(max_length=40, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


def on_user_logged_in(sender, request, user, **kwargs):
    user.is_user_logged_in = True

user_logged_in.connect(on_user_logged_in)
