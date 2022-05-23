# URL

## SERVER URL

### main

- admin
- accounts
- movies
- crews

### accounts

| url                                                          | 설명        | 데이터                                                       | HTTP |
| ------------------------------------------------------------ | ----------- | ------------------------------------------------------------ | ---- |
| accounts/signup/                                             | 회원가입    | email,password1,password2                                    | POST |
| accoutns/login/                                              | 로그인      | email,password                                               | POST |
| accounts/jwt/                                                | jwt발급     | email,password                                               | POST |
| accounts/profile_create                                      | 프로필 생성 | nickname,image,backdrop,intoduce,<br />birth,gender,location1,location2 | POST |
| accounts/profile/\<int:user_pk>                              | 프로필 조회 | nickname,image,backdrop,intoduce,<br />birth,gender,location1,location2 | GET  |
| accounts/genrelist/                                          | 장르 조회   | genre_name                                                   | GET  |
| accounts/selectgenre/<br />\<int:genre1>/\<int:genre2>/\<int:genre3> | 장르 선택   | genre_pk                                                     | POST |
|                                                              |             |                                                              |      |
|                                                              |             |                                                              |      |

### Movies

| url                                              | 설명               | 데이터 | HTTP |
| ------------------------------------------------ | ------------------ | ------ | ---- |
| movies/\<int:movie_pk>/                          | 영화 디테일조회    |        | GET  |
| movies/\<int:movie_pk>/like/                     | 영화 좋아요 누르기 |        | POST |
| movies/\<int:movie_pk>/reviews/                  | 영화 리뷰 조회     |        | GET  |
| movies/\<int:movie_pk>/reviews/                  | 영화 리뷰 작성     |        | POST |
| movies/\<int:movie_pk>/reviews/\<int:review_pk>/ | 영화 리뷰 업데이트 |        | PUT  |
| movies/\<int:movie_pk>/reviews/\<int:review_pk>/ | 영화 리뷰 삭제     |        | POST |
| movies/\<int:movie_pk>/\<int:crew_pk>/           | 크루 영화에 추가   |        | POST |
| movies/crew/\<int:crew_pk>/                      | 크루 영화 조회     |        | GET  |
|                                                  |                    |        |      |

### Crews

| url                                                          | 설명             | 데이터 | HTTP |
| ------------------------------------------------------------ | ---------------- | ------ | ---- |
| crews/                                                       | 크루 리스트      |        | GET  |
| crews/crew_creqte                                            | 크루 만들기      |        | POST |
| crews/\<int:crew_pk>                                         | 크루 상세정보    |        | GET  |
| crews/\<int:crew_pk>                                         | 크루 정보 갱신   |        | PUT  |
| crews/\<int:crew_pk>                                         | 크루 가입        |        | POST |
| crews/\<int:crew_pk>/articles/                               | 크루 게시글 조회 |        | GET  |
| crews/\<int:crew_pk>/articles/                               | 크루 게시글 작성 |        | POST |
| crews/\<int:crew_pk>/articles/\<int:article_pk>              | 게시글 상세조회  |        | GET  |
| crews/\<int:crew_pk>/articles/\<int:article_pk>              | 게시글 정보 변경 |        | PUT  |
| crews/\<int:crew_pk>/articles/\<int:article_pk>              | 게시글 삭제      |        | POST |
| crews/articles/\<int:article_pk>/comments/                   | 댓글 작성        |        | POST |
| crews/articles/\<int:article_pk>/comments/                   | 댓글 리스트 조회 |        | GET  |
| crews/articles/\<int:article_pk>/comments/\<int:comment_pk>/ | 댓글 수정        |        | PUT  |
| crews/articles/\<int:article_pk>/comments/\<int:comment_pk>/ | 댓글 삭제        |        | POST |

