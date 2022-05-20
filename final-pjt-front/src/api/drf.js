const HOST = 'http://localhost:8000/api/v1/'

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
    reviews: movieId => HOST + MOVIES + `${movieId}/` + REVIEWS,
    review: (movieId, reviewId) => HOST + MOVIES + `${movieId}/` + REVIEWS + `${reviewId}`,
  },
  crews:{
    crews: () => HOST + CREWS,
    crew: crewId => HOST + CREWS + `${crewId}/`,
    withMovie: movieId => HOST + MOVIES + `${movieId}/` + `with/`,
    articles: crewId => HOST + CREWS + `${crewId}` + ARTICLES,
    article : (crewId, articleId) => HOST + CREWS + `${crewId}` + ARTICLES + `${articleId}`,
  }
}