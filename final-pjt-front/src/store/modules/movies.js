import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default{
  state: {
    token: localStorage.getItem('jwt') || '',
    topRatedMovies:[],
    myMovies: [],
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
    reviews:[],
    filmos:[],
    actorInfo:{},
    weather:'',
    weatherMovies: [],
    Thunderstorm:[274855,435,216282,745881,30497,674,397837,293670,430040],
    Clear:[448491,43949,460668,277834,212778,84111,467909,269149,16859,398818],
    Snow:[79680,38,47002,578209,336026,1581,24,38142,4550,109445,330457,321612],
    Rain:[59436,153,26935,42190,381284,489,122906,499028,293670,338729,11036,44632,315846,420817],
    Clouds:[313369,568160,579188,640,205596,20342,581390,8966],
    Drizzle:[59436,153,26935,42190,381284,489,122906,499028,293670,338729,11036,44632,315846,420817],
    unknown:[37280,128881,605193],
    groupMovies: [],


  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    topRatedMovies: state => state.topRatedMovies,
    authHeader2: state => ({ Authorization: `JWT ${state.token}`}),
    reviews: state => state.reviews,
    filmos: state => state.filmos,
    actorInfo: state=> state.actorInfo,
    weather: state => state.weather,
    weatherMovies: state => state.weatherMovies,
    groupMovies: state=> state.groupMovies,
   
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie= movie,
    SET_MOVIE_REVIEWS: (state, reviews) => (state.reviews = reviews),
    GET_MOVIE_REVIEWS: (state, reviews) => (state.reviews = reviews),
    SET_TOP_RATED_MOVIES: (state, movies) => (state.topRatedMovies = movies),
    SET_FILMOS: (state, filmos) => (state.filmos = filmos),
    SET_ACTOR_INFO: (state, info) => (state.actorInfo= info),
    SET_WEATHER: (state, weather) => (state.weather = weather),
    SET_WEATHER_MOVIES: (state, movies) => (state.weatherMovies = movies),
    ADD_WEATHER_MOVIES: (state, movie) => {
      (state.weatherMovies.push(movie))
    },
    SET_GROUP_MOVIES: (state, movies) => (state.groupMovies = movies),      
  
    
  },

  actions: {
    fetchMovie({commit,getters}, movieId){
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader,
        
      })
      .then(res => {
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

    createReview({commit, getters}, {movieId, content, rate}) {
      const review = {content, rate}
      axios({
        url: drf.movies.reviews(movieId),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
      .then(res => {
        // console.log(res.data)
        commit('SET_MOVIE_REVIEWS', res.data)
      })
      .catch(err => console.error(err.response))
    },

    readReviews({ commit, getters}, movieId) {
      axios({
        url: drf.movies.reviews(movieId),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('GET_MOVIE_REVIEWS', res.data)
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
        // console.log(res)
        commit ('SET_TOP_RATED_MOVIES', res.data.results)
      })
    },

    getActorInfo({commit}, castId){
      const API_URL = `https://api.themoviedb.org/3/person/${castId}`
      const params = {
        api_key: '473836c79a1fc815410e8bc162e748cd',
        language: 'ko-KR',
      }
      axios({
        mehtod: 'get',
        url: API_URL,
        params
      })
      .then(res => {
        commit('SET_ACTOR_INFO', res.data)
        // console.log(res.data)
      })
    },

    getCastDetail({commit},castId){
      const API_URL = `https://api.themoviedb.org/3/person/${castId}/movie_credits`
      const params = {
        api_key: '473836c79a1fc815410e8bc162e748cd',
        language: 'ko-KR',
      }
      axios({
        mehtod: 'get',
        url: API_URL,
        params
      })
      .then(res => {
        commit('SET_FILMOS', res.data)
        // console.log(res.data)
      })
    },

    fetchWeatherMovie({commit,getters}, movieId){
      axios({
        url: drf.movies.movie(movieId),
        method: 'get',
        headers: getters.authHeader2,
      })
      .then(res => {
        console.log(res.data)
        commit('ADD_WEATHER_MOVIES', res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },

    removeMovies({commit}){
      commit('SET_WEATHER_MOVIES', [])
    },

    getWeather({commit, state, dispatch}, location){
      const API_KEY = '343c1608f7c4aa62ef8a1d76113b002d'
      const API_URL = `https://api.openweathermap.org/data/2.5/weather?q=${location}&lang=kr&appid=${API_KEY}`
      axios({
        method:'get',
        url: API_URL,
      })
      .then(res => {
        dispatch('removeMovies')
        commit('SET_WEATHER', res.data.weather[0].main)
        const nowweather = state.weather
        if (nowweather==='Thunderstorm'){
          const movieids = state.Thunderstorm
          for (let index = 0; index < movieids.length; index++) {
            this.fetchWeatherMovie(movieids[index])
          }
        } else if (nowweather==='Rain'){
          const movieids = state.Rain
          for (let index = 0; index < movieids.length; index++) {
            this.fetchWeatherMovie(movieids[index])
          }
        } else if (nowweather==='Clear'){
          const movieids = state.Clear
          for (let index = 0; index < movieids.length; index++) {
            console.log(movieids[index])
            this.fetchWeatherMovie(movieids[index])
            
          }
        } else if (nowweather==='Snow'){
          const movieids = state.Snow
          for (let index = 0; index < movieids.length; index++) {
            this.fetchWeatherMovie(movieids[index])
          }
        } else if (nowweather==='Drizzle'){
          const movieids = state.Drizzle
          for (let index = 0; index < movieids.length; index++) {
            this.fetchWeatherMovie(movieids[index])
          }
        } else if (nowweather==='Clouds'){
          const movieids = state.Clouds
          for (let index = 0; index < movieids.length; index++) {
            dispatch('fetchWeatherMovie', movieids[index])
          }
        } else {
          console.log('else')
        }
        
      })
      .catch(err => console.error(err.response))
    },

    getGroupMovies({commit, getters}){
      const num = _.random(1,6)
      axios({
        url: drf.movie(num),
        method: 'get',
        headers: getters.authHeader2
      })
      .then(res => {
        commit('SET_GROUP_MOVIES', res.data)
      })
      .catch(err => console.error(err.response))
      
    },


  },
}