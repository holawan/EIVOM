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
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(300, 300)],
        format='JPEG',
        options={'quality': 60}
    )
    crew_location = models.CharField(max_length=4)
    crew_leader = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='leader_user')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)
    movies = models.ManyToManyField(Movie,blank=True)

    def __str__(self) :
       return self.crewname

class CrewArticle(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    crew = models.ForeignKey(Crew,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

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

   def __str__(self) :
       return self.content