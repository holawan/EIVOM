# 서버개발 일지

## 0519

### 시작 

- SECRET_KEY 비공개 

- ERD를 바탕으로 모델을 만들고, REST_API로 보내려고 한다. 
- User모델은 Abstract 참조해서 커스텀 가능하게 했다.
- rest_framework에 관한 패키지들을 설치하고, allauth, CORS에 관한 설정도 마쳤다.
- url 설정을 진행해서, 간단히 확인을 했더니 잘 나왔다.

### Profile 모델 만들기 

#### 미디어파일 ?

- 처음에 TMDB 이미지파일의 사이즈가 약간 제멋대로라, Django에서 resizing을 하려고 해서, imagekit을 설치하고, STATIC,MEDIA 옵션도 추가했는데 생각해보니 front는 Vue에서 하니까, 그냥 api 받아서 url만 넘겨줘야겠다고 생각이 들었다..
- 따라서 이미지필드를 쓰지 않고 그냥 text로 받아야겠다.

- 근데, 생각해보니 프로필이랑 크루 이미지는 어떻게 하지?라는 생각이 들었다. 알아보니, db에는 url만 저장하고, 서버에서 이미지를 가져오는거라(?) 문제는 없을 것 같다고 생각했다.

#### ManyToMany Field 추가

- admin에서 ManyToManyField를 선택안하고 생성을 하니, 제출이 되지 않았다. 그래서 blank=True 옵션을 주니까 제출이 되었다. 
- 왜 template에서 제출할때는 명시 안해줘도 되는데, admin에서는 blank=True를 주면 안될까? 나도 모르겠다

#### symmetrical

- ManyToMany Field를 자기 자신과 할 경우에는 symmetrical이라는 옵션을 사용할 수 있다. 이건 기본적으로 True인데 True일 경우를 가정하면, 만약 내가 다른 사람한테 팔로우를 걸면 그사람도 내가 자동으로 맞팔이 된다. 
- 근데, False로 하면 그사람이 팔로우한다고 맞팔되는게 아니라고 한다.  



