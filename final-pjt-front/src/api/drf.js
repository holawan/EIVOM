const HOST = 'http://localhost:8000/'

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
    createProfile: () => HOST + ACCOUNTS + 'create_profile/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: movieId => HOST + MOVIES + `${movieId}/`,
    likeMovie: movieId => HOST + MOVIES + `${movieId}/` + 'like/',
    addMovie: (movieId, crewId) => HOST + MOVIES+ `${movieId}` + `${crewId}` + 'add/',
    reviews: movieId => HOST + MOVIES + `${movieId}/` + REVIEWS,
    review: (movieId, reviewId) => HOST + MOVIES + `${movieId}/` + REVIEWS + `${reviewId}/`,
  },
  crews:{
    create: ()=> HOST + CREWS + 'create/',
    register: crewId => HOST + CREWS + `${crewId}`+ 'register/',
    crews: () => HOST + CREWS,
    crew: crewId => HOST + CREWS + `${crewId}/`,
    withMovie: movieId => HOST + MOVIES + `${movieId}/` + `with/`,
    articles: crewId => HOST + CREWS + `${crewId}` + ARTICLES,
    article : (crewId, articleId) => HOST + CREWS + `${crewId}` + ARTICLES + `${articleId}/`,
    reviews: (crewId, articleId) => HOST + CREWS + `${crewId}` + ARTICLES + `${articleId}` + REVIEWS,
    review: (crewId, articleId, reviewId) => HOST + CREWS + `${crewId}` + ARTICLES + `${articleId}` + REVIEWS + `${reviewId}/`,
  }
}