import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import _ from 'lodash'

export default{
  state: {
    token: localStorage.getItem('jwt') || '',
    topRatedMovies:[],
    myMovies: [],
    crewMovies: [],
    boxOfficeMovies:[],
    RecActorMovies:[],
    RecForYouMovies:[],
    RecGenreMovies:[],
    RecHighlyViewMovies:[],
    RecMasterPieceMovies:[],
    RecSimilarMovies:[],
    RecWeatherMovies:[],
    RecWeeklyMovies:[],
    movies: [],
    movie: {},
    selectedMovie: null,
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    topRatedMovies: state => state.topRatedMovies,
    authHeader2: state => ({ Authorization: `JWT ${state.token}`}),
   
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie= movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    SET_TOP_RATED_MOVIES: (state, movies) => (state.topRatedMovies = movies),
    
  },

  actions: {
    fetchMovie({commit,getters}, movieId){
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
        
      })
      .then(res => {
        console.log(res)
        commit('SET_MOVIE', res.data)

      })
      .catch(err => {
        console.error(err.response)
        if (err.response.status === 404){
          router.push({name:'NotFound404'})
        }
      })
    },

    likeMovie({commit, getters }, movieId) {
      axios({
        url: drf.movies.likeMovie(movieId),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.error(err.response))
    },

    addMovie({commit, getters }, {movieId, crewId}){
      axios({
        url: drf.movies.addMovie(movieId, crewId),
        method:'post',
        headers: getters.authHeaders,
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => console.err(err.response))
    },

    createReview({commit, getters}, {movieId, content}) {
      const review = {content}
      axios({
        url: drf.movies.reviews(movieId),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIE_REVIEW', res.data)
      })
      .catch(err => console.error(err.response))
    },

    getTopRatedMovie({commit}){
      const API_URL = 'https://api.themoviedb.org/3/movie/top_rated'
      const params = {
        api_key : '473836c79a1fc815410e8bc162e748cd',
        language : 'ko-KR' ,
        page : 1
      }
      axios({
        method: 'get',
        url :API_URL,
        params
      })
      .then(res => {
        console.log(res)
        commit ('SET_TOP_RATED_MOVIES', res.data.results)
      })
    },
  },
}