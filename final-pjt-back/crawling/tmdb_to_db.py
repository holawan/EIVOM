import json
import environ
import requests

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env()


TMDB_API_KEY = env('TMDB_API_KEY')


def get_genre_datas() :
    BASE_URL = "https://api.themoviedb.org/3/genre/movie/list"
    total_genre = []

    request_url = f"{BASE_URL}?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()
    print(genres)
    print('-----------------------------')
    for genre in genres['genres'] :
        print(genre)
        fields = {
            'id' : genre['id'],
            'name' : genre['name']
        }
        print(fields)
        print('----------------------------------')
        data = {
            "pk" : genre['id'],
            "model" : "movies.Genre",
            "fields" : fields
        }
        print(data)
        print('------------------------------')
        total_genre.append(data)
        print(total_genre)
        print('------------------------------------------')
    with open("genre_data.json","w",encoding="utf-8") as w:
        json.dump(total_genre,w,indent="\t", ensure_ascii=False)

get_genre_datas()
# def get_movie_datas() :
#     total_data_id = []
#     total_movie_data = []
#     BASE_URL = "https://api.themoviedb.org/3/movie/"
#     BASE_URL2 = "https://api.themoviedb.org/3/person/"

#     #1페이지부터 738페이지까지 popular movie 가져와서 id만 취하기 
#     #501페이지부터는 에러가 발생해 500까지로 수정 
#     cnt = 0
#     for i in range(1,501) :
#         cnt += 1 
#         print(f'page_id:{cnt}')
#         #popular 요청 
#         request_url = f"{BASE_URL}popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}&region=KR"
#         #movies에 저장 
#         movies = requests.get(request_url).json()
#         # print(movies)

#         #result를 돌면서 id만 저장 
#         for movie in movies['results'] :
#             total_data_id.append(movie['id'])
#     cnt = 0
#     #id들을 돌면서detail 정보 가져오기 
#     for movie_id in total_data_id :
#         cnt += 1 
#         print(f'movie_detail:{cnt}')
#         # detail 정보 요청할 url 
#         request_url = f"{BASE_URL}{movie_id}?api_key={TMDB_API_KEY}&language=ko-KR"
#         print(request_url)
#         #json으로 가져와서 
#         movie = requests.get(request_url).json()
#         print(movie)
#             #genre_id형태가 json이라 모델과 형식이 맞지 않아,id만 가져오기 위해 필드 따로 생성
#         genre_ids = [] 
        
#         for genre in movie['genres'] :
#             genre_ids.append(genre['id'])
#         print(genre_ids)
#         fields = {
#         'id' : movie['id'],
#         'title' : movie['title'],
#         'original_title' : movie['original_title'],
#         'poster_path' : movie['poster_path'],
#         'backdrop_path' : movie['backdrop_path'],
#         'overview' : movie['overview'],
#         'release_date' : movie['release_date'],
#         'vote_count' : movie['vote_count'],
#         'vote_average' : movie['vote_average'],
#         'popularity' : movie['popularity'],
#         'runtime' : movie['runtime'],
#         'tagline' : movie['tagline'],
#         'genres' :genre_ids,
#         'director': '',
#         'actor_id' : [],
#         'actors': [],
#         'actors_path' : [],

#     }

#         data = {
#             "pk" : movie['id'],
#             "model" : "movies.Movie",
#             "fields" : fields
#         }
#         total_movie_data.append(data)
#     # 영화 id를 가져와서 
#     for data in total_movie_data :
#         movie_id = data['fields']['id']
#         #크레딧을 검색한다.
#         credit_request_url = f"{BASE_URL}{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR"
#         #크레딧 info를 불러오고 
#         credit_info = requests.get(credit_request_url).json()
#         #배우를 최대 15명까지로 넣기로하고, 해당 배우 목록들을 돌면서,
#         for cast in credit_info['cast'][:15] :
#             #id를 가져와서 
#             cast_id = cast['id']
#             print(cast_id)
#             # 배우의 id로 디테일 정보에 접근한다.
#             name_request_url = f"{BASE_URL2}{cast_id}?api_key={TMDB_API_KEY}&language=ko-KR"
#             actor = requests.get(name_request_url).json()
#             # 배우 id를 모델에 추가 
#             data['fields']['actor_id'].append(cast_id)
#             #배우에 잘 알려진 이름을 모델에 추가 
#             if actor['also_known_as'] :
#                 data['fields']['actors'].append(actor['also_known_as'][0])
#             else :
#                 data['fields']['actors'].append(cast['name'])
#             #배우의 프로필사진을 모델에 추가 
#             if actor['profile_path'] :
#                 data['fields']['actors_path'].append(actor['profile_path'])
#             else :
#                 data['fields']['actors_path'].append('')
#         #감독이름을 모델에 추가 
#         if credit_info['crew']:
#             data['director'] = credit_info['crew'][0]['name']
    
#     with open("movie_data.json", "w", encoding="utf-8") as w:
#         json.dump(total_movie_data, w, indent="\t", ensure_ascii=False)




    

# get_genre_datas()
# get_movie_datas()