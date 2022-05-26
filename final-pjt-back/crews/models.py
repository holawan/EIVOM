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
        upload_to='thumbnails/crew/image/',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60},
         default='media/crew/크루기본.png'
    )
    crew_backdrop = ProcessedImageField(
        blank=True,null=True,
        upload_to='thumbnails/crew/backdrop/',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60},
        default='media/crew/크루배경기본.png'
    )
    
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
    crew_location1 = models.CharField(max_length=10,choices=LOCATION_COHICES,null=True,blank=True)
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
   article = models.ForeignKey(CrewArticle,on_delete=models.CASCADE,related_name='comments')
   #리뷰내용
   content = models.CharField(max_length=100)
   #작성시간
   created_at = models.DateTimeField(auto_now=True)
   updated_at = models.DateTimeField(auto_now_add=True)

   def __str__(self) :
       return self.content
