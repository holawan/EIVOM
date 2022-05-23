const HOST = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const CREWS = 'crews/'
const ARTICLES = 'articles/'


export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    createProfile: () => HOST + ACCOUNTS + 'profile_create/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    getJwtToken: () => HOST + ACCOUNTS + 'jwt/',
    profile: user_pk => HOST + ACCOUNTS + 'profile/' + `${user_pk}/`,
    genrelist: () => HOST + ACCOUNTS + 'genrelist/',
    selectGenre: (genre1, genre2, genre3) => HOST + ACCOUNTS + 'selectgenre/' + `${genre1}/` + `${genre2}/` + `${genre3}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: movie_pk => HOST + MOVIES + `${movie_pk}/`,
    likeMovie: movie_pk => HOST + MOVIES + `${movie_pk}/` + 'like/',
    addMovie: (movie_pk, crewId) => HOST + MOVIES+ `${movie_pk}` + `${crewId}` + 'add/',
    reviews: movie_pk => HOST + MOVIES + `${movie_pk}/` + REVIEWS,
    review: (movie_pk, review_pk) => HOST + MOVIES + `${movie_pk}/` + REVIEWS + `${review_pk}/`,
  },
  crews:{
    create: ()=> HOST + CREWS + 'crew_create/',
    register: crewId => HOST + CREWS + `${crewId}`+ 'register/',
    crews: () => HOST + CREWS,
    crew: crewId => HOST + CREWS + `${crewId}/`,
    withMovie: movieId => HOST + MOVIES + `${movieId}/` + `with/`,
    articles: crewId => HOST + CREWS + `${crewId}` + ARTICLES,
    article : (crewId, articleId) => HOST + CREWS + `${crewId}` + ARTICLES + `${articleId}/`,
    reviews: (crewId, articleId) => HOST + ARTICLES + `${articleId}` + REVIEWS,
    review: (crewId, articleId, reviewId) => HOST + ARTICLES + `${articleId}` + REVIEWS + `${reviewId}/`,
  }
}