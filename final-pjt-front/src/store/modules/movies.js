import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

// import _ from 'lodash'

export default{
  state: {
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
   
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie= movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.movie.reviews = reviews),
    
  },

  actions: {
    fetchMovie({commit, getters}, movieId){
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MOVIE', res.data))
      .catch(err => {
        console.err(err.response)
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
    }
  },
}