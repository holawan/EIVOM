from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from movies.models import Movie
# Create your models here.
class Crew(models.Model) :
    crewname = models.CharField(max_length=10,unique=True)
    crewintro = models.CharField(max_length=30)
    crew_image = ProcessedImageField(
        blank=True,null=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60}
    ),
    crew_backdrop = ProcessedImageField(
        blank=True,null=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60},
        default='media/김태리.jpg'
    ),
    
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
    crew_location1 = models.CharField(max_length=10,choices=LOCATION_COHICES,null=True,blank=True)
    crew_location2 = models.CharField(max_length=5,null=True,blank=True)
    crew_leader = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='leader_user')
    crew_users = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='users_crew')
    movies = models.ManyToManyField(Movie,blank=True,related_name='crews')

    def __str__(self) :
       return self.crewname

class CrewArticle(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
       return self.title


class CrewReview(models.Model) :
    #리뷰작성자
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   #리뷰를 작성하려는 영화
   article = models.ForeignKey(CrewArticle,on_delete=models.CASCADE)
   #리뷰내용
   content = models.CharField(max_length=100)
   #작성시간
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) :
       return self.content
