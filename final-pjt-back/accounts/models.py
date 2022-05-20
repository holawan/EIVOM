from django.db import models
#Django 
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

# Create your models here.

class User(AbstractUser) :
    username = None
    email = models.EmailField(_('email address'),unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    objects = CustomUserManager()
    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)


    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self) :
        return self.email
class Profile(models.Model) :
    #Profle과 user는 1대1 관계 
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='profile')
    #닉네임 
    nickname = models.CharField(max_length=10,unique=True)
    #프사
    image = ProcessedImageField(
    blank=True,
    upload_to='thumbnails/',
    processors=[Thumbnail(300, 300)],
    format='JPEG',
    options={'quality': 60})
    #배경사진
    backdrop = ProcessedImageField(
    blank=True,
    upload_to='thumbnails/',
    processors=[Thumbnail(1200, 800)],
    format='JPEG',
    options={'quality': 60})
    #소개말
    introduce = models.CharField(max_length=100)
    #생년월일
    birth = models.DateField()
    #성별
    GENDER_CHOICES = (
        (0,'남성'),
        (1,'여성')
    )
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    #도/특별시/광역시
    LOCATION_COHICES = (
        (11,'서울특별시'),
        (21,'부산광역시'),
        (22,'대구광역시'),
        (23,'인천광역시'),
        (24,'광주광역시'),
        (25,'대전광역시'),
        (26,'울산광역시'),
        (29,'세종특별자치시'),
        (31,'경기도'),
        (32,'강원도'),
        (33,'충청북도'),
        (34,'충청남도'),
        (35,'전라북도'),
        (36,'전라남도'),
        (37,'경상북도'),
        (38,'경상남도'),
        (39,'제주특별자치도'),

    )
    location1 = models.CharField(max_length=10,choices=LOCATION_COHICES)
    #시/군/구
    location2 = models.CharField(max_length=5)
    def __str__(self) :
        return self.nickname
