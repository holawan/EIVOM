# 서버개발 일지

## 0519

### 시작 

- SECRET_KEY 비공개 

- ERD를 바탕으로 모델을 만들고, REST_API로 보내려고 한다. 
- rest_framework에 관한 패키지들을 설치하고, allauth, CORS에 관한 설정도 마쳤다.
- url 설정을 진행해서, 간단히 확인을 했더니 잘 나왔다.

### 미디어파일 ?

- 처음에 TMDB 미디어파일이 제멋대로라, Django에서 resizing을 하려고 해서, imagekit을 설치하고, STATIC,MEDIA 옵션도 추가했는데 생각해보니 front는 Vue에서 하니까, 그냥 url만 넘겨줘야겠다고 생각이 들었다..
- 따라서 이미지필드를 쓰지 않고 그냥 text로 받아야겠다.