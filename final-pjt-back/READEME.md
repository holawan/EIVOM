# 서버개발 일지

## 0519

### 시작 

- SECRET_KEY 비공개 

- ERD를 바탕으로 모델을 만들고, REST_API로 보내려고 한다. 
- User모델은 Abstract 참조해서 커스텀 가능하게 했다.
- rest_framework에 관한 패키지들을 설치하고, allauth, CORS에 관한 설정도 마쳤다.
- url 설정을 진행해서, 간단히 확인을 했더니 잘 나왔다.

### 모델 만들기 

#### 미디어파일 ?

- 처음에 TMDB 이미지파일의 사이즈가 약간 제멋대로라, Django에서 resizing을 하려고 해서, imagekit을 설치하고, STATIC,MEDIA 옵션도 추가했는데 생각해보니 front는 Vue에서 하니까, 그냥 api 받아서 url만 넘겨줘야겠다고 생각이 들었다..
- 따라서 이미지필드를 쓰지 않고 그냥 text로 받아야겠다.

- **근데, 생각해보니 프로필이랑 크루 이미지는 어떻게 하지?라는 생각이 들었다. 알아보니, db에는 url만 저장하고, 서버에서 이미지를 가져오는거라(?) 문제는 없을 것 같다고 생각했다.**

#### ManyToMany Field 추가

- admin에서 ManyToManyField를 선택안하고 생성을 하니, 제출이 되지 않았다. 그래서 blank=True 옵션을 주니까 제출이 되었다. 
- 왜 template에서 제출할때는 명시 안해줘도 되는데, admin에서는 blank=True를 주면 안될까? 나도 모르겠다

#### symmetrical

- ManyToMany Field를 자기 자신과 할 경우에는 symmetrical이라는 옵션을 사용할 수 있다. 이건 기본적으로 True인데 True일 경우를 가정하면, 만약 내가 다른 사람한테 팔로우를 걸면 그사람도 내가 자동으로 맞팔이 된다. 
- 근데, False로 하면 그사람이 팔로우한다고 맞팔되는게 아니라고 한다.  

## 0520

### 소셜로그인하기 

- 소셜로그인을 하기 위해 다양한 정보를 찾아봤는데, DRF에서는 거의 JWT를 썼다. 그래서, 교수님께 여쭤봤는데 JWT를 많이 쓰고, 기존 세션방식 인증과 크게 다르지 않다고 해서 쓰기로 했다.

- 먼저 Google 소셜로그인을 했는데, 계속 리다이렉션 오류가 발생했다. 그러다가, REDITECT_URI를 요청하는대로 맞춰줬더니 로그인이 되었다. 근데 이거 계속 수정하는데 3시간정도 걸렸다.
- 카카오 소셜로그인으로 넘어갔다. 근데, 계속 REDIRECT_URI 에러가 뜨면서 갑자기 구글 소셜로그인도 안됐다. 아니 이해할수가 없다... 이게 다 공부를 안하고 그냥 코드를 가져와서 써서 그런 것 같다 ㅠ 
- 그러다가 한 2시간정도 카카오에서 에러만 나와서 그냥 코드 다 삭제하고 처음부터 다시 천천히 따라쳤는데도, 같은 오류가 나왔다. 
- django 서버 url이 localhost:8000이랑 127.0.0.1:8000 두개가 있는데 심지어 allauth에서는 google권장이랑 kakao 권장이 달랐다. 그래서 이제 모르겠다는 식으로 REDIRECT_URI와 서버 등록할때 둘다 넣어버렸다. 
- 그랬는데, 뭔가 갑자기 구글이 됐다.
- 카카오는 계속 안되는거를 print하면서 역추적하다보니까, 내 IP로는 요청을 보낼수 없다고 나왔다.
  - 돌이켜보니, 내가 고급설정에서 URL요청할 수 있는 주소를 설정할때 내 127.0.0.1:800으로 해놔서 그런 것 같았다.
- 그래서 고급설정을 비웠더니 정상적으로 됐다.
- 근데, 아직도 요청을 계속 보내고 로그아웃하고 로그인하고 해서 그런지,, 갑자기 안될때도 있다. 
- 하지만 기도메타로 내일은 된다고 생각해야겠다



### 영화 가져오기

- TMDB에서 영화를 가져올 때, actor와 director를 가져오면서 actor이름은 also_known_as로 가져오려고 했다.
- 따라서 요청 방식은 먼저 genre는 따로 가져온다
- 영화를 가져올때는 popula movie에 500페이지 요청을 보내서 10000개의 영화 id만 가져온다.
- 그 10,000개의 영화id를 detail로 요청 보내서 detail 정보를 가져온다
- detail 정보를 가져온 후 movieid로 cast에 요청을 보내서 actor 15명과 감독 1명을 가져온다. 
- actor는 다시 people/actor_id로 요청을 보내서 also_known_as를 가져온다.
- 따라서 최대 500+10000+10000*16번으로 161500번 요청을 보낸다. 
- 그러다보니 API가 도중에 차단당하는 경우가 몇 번 발생했다.
- 그리고 also_known_as가 json decoding 과정에서 에러가 발생해서 중간에 통신이 끊겼었다.
  - try,expect로 분기 처리를 해줘서 해결했다.

#### 영화를 잘 받아왔고, 모델에 성공적으로 저장되었다!! 



### JWT logout

- JWT는 너무 어렵다....

- 잘 안배워서 뭔지 좀 어려운데, 일단 logout을 할 때 refresh token을 담아서 해줘야 로그아웃이 잘 된다.

- 근데 Django DRF server에서는 POST로 logout을 보낼 때 

  - {

      "detail": "Refresh token was not included in request data."

    }

  - 이런 에러가 뜨긴 하지만 로그아웃이 된다.

- 근데 POSTMAN에서는 로그아웃이 안된다. 원래 포스트맨은 로그인 로그아웃이 안되는건가요 ?

## 0521

### serializer

- 직렬화를 이용해서 client에 데이터를 넘겨줘야하는데, serializer에 여러 모델들을 추가해서 한 번에 정보를 받게 (예를 들어, 프로필에서 user user에서 user가 좋아하는 장르)해야하는지 좀 헷갈렸다. 
- 많은 정보를 한 번에 주는 경우가 아니라면 한 번에 serializer에 여러 데이터를 실어줘도 좋을 것 같다.

### genre_select

- 유저가 선호하는 장르를 기반으로 추천시스템을 구현하려 했는데, 처음에는 url을 3개로 제한해서 구성했다

  ```python
  #accounts/urls.py
  
  path('selectgenre/<int:genre1>/<int:genre2>/<int:genre3>/',views.genre_add),
  ```

- 그런데 생각해보니, 이럴 필요가 없이 add/remove로  누르면 선호장르에 추가 다시 누르면 해제되게 하고 frontend에서도 이벤트를 주면 여러 장르를 선택하게 할 수도 있고 선택하지 않을 수도 있어서 유저 입장에서 더 좋을 것이라 생각했다. 

- 따라서 url과 views.py를 변경했다.

  ```python
  #accounts/urls.py
  path('selectgenre/<int:genre>/',views.genre_add),
  
  #accounts/views.py
  @api_view(['POST'])
  def genre_add(request,genre):
      genre = get_object_or_404(Genre,pk=genre) 
      user = request.user 
      if user.like_genres.filter(pk=genre.pk).exists():
          user.like_genres.remove(genre)
          serializer = UserSerilaizer(user)
          return Response(serializer.data,status=status.HTTP_201_CREATED)
      else :
          user.like_genres.add(genre)
          serializer = UserSerilaizer(user)
          return Response(serializer.data,status=status.HTTP_201_CREATED)
  
  ```

### 소셜로그인

- 소셜로그인을 계속 시도했는데, 잘 안되었다.
- 그 원인을 몇가지 찾아봤다.
  1. 공식문서를 참고하지 않고 블로그에 있는 다른 프로젝트에서 진행한 정보를 참고해서 진행하다 보니, 내 프로젝트와 맞지 않는 부분들이 있어서 오류 발생
  2. 소셜로그인의 중심이 django 서버가 아닌 Vue.js에서 진행되고, django에서는 토큰으로 인증과 user테이블에 정보를 저장해야하는데, drf자체에서 소셜로그인을 만듬
  3. 즉, 너무 급하게 진행하려함
- Django 자체에서는 소셜로그인이 잘 되었던 기억이 있었는데, 초기에 server 작업만 하다보니 vue에서 sociallogin을 해야하는걸 생각하지 못했다.
- 따라서, 공식문서를 참고해서 Vue에서 소셜로그인을 시도했는데, 자꾸 구글 클라우드 플랫폼에서도 에러가 발생하고 CORS 에러가 발생했다.
- 정말 하고 싶지만 이것만 매달리기에는 해야할 작업이 많았기 때문에 기본적인 기능을 모두 구현한 후 소셜로그인을 진행하기로 페어와 협의했다.



## 0522

### serializer

- Review Seliarlizer를 작성하는 과정에서 related_name에서 불편함을 느꼈다. 원래 1:N 필드에서 역참조를 할 때는 대부분 set을 사용하고 M:N 필드에서는 reated_name을 설정하는 것이 일반적이라고 들었지만, set을 사용하는게 seliarizer에서 가끔 에러가 발생하는 경우가 있었다.
- 아무래도 신경쓸게 많다보니 사소한 실수가 있었던 것 같다.
- 그래서 그냥 모든 관계형 테이블에 related_name을 설정했다. 뭔가, 마음이 편해졌다..

### ImageField

- 프로필이나 커버사진을 만들 때 원래 서버에 등록 시 Tumbnail을 이용해 먼저 잘라서 media 폴더에 저장했었다.
- frontend에서 사진이 아예 잘려버리는 문제가 있어서, 직접 자르겠다고 요청해주셨고, 따라서 필드에 thumbnail을 없앴다.
