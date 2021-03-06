const HOST = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const CREWS = 'crews/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'


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
    selectGenre: (genre) => HOST + ACCOUNTS + 'selectgenre/' + `${genre}/`,
    getCrew: user_pk => HOST + ACCOUNTS + 'getcrew/' + `${user_pk}/`
  },
  movies: {
    movies: () => HOST + MOVIES,
    movie: movie_pk => HOST + MOVIES + `${movie_pk}/`,
    likeMovie: movie_pk => HOST + MOVIES + `${movie_pk}/` + 'like/',
    addMovie: (movie_pk, crew_pk) => HOST + MOVIES+ `${movie_pk}/` + `${crew_pk}/` + 'add/',
    reviews: movie_pk => HOST + MOVIES + `${movie_pk}/` + REVIEWS,
    review: (movie_pk, review_pk) => HOST + MOVIES + `${movie_pk}/` + REVIEWS + `${review_pk}/`,
    cluster: cluster => HOST + MOVIES + 'cluster_recommend/' +`${cluster}/`,
    genreRec: () => HOST + MOVIES + 'genre_recommend/',
    viewCount: () => HOST + MOVIES + 'view_count_recommend/',
    reviewEdit : (movie_pk,review_pk) => HOST + MOVIES + `${movie_pk}/reviews/${review_pk}/`,
  },
  crews:{
    create: ()=> HOST + CREWS + 'crew_create/',
    crews: () => HOST + CREWS,
    crew: crew_pk => HOST + CREWS + `${crew_pk}/`,
    withMovie: movieId => HOST + MOVIES + `${movieId}/` + `with/`,
    articles: crew_pk => HOST + CREWS + `${crew_pk}/` + ARTICLES,
    article : (crew_pk, article_pk) => HOST + CREWS + `${crew_pk}/` + ARTICLES + `${article_pk}/`,
    comments: (crew_pk, article_pk) => HOST + CREWS + `${crew_pk}/` + ARTICLES + `${article_pk}/` + COMMENTS,
    comment: (article_pk,crew_pk, comment_pk) => HOST + CREWS + `${crew_pk}/` + ARTICLES + `${article_pk}/` + COMMENTS + `${comment_pk}/`,
  }
}