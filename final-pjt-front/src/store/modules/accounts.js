import router from "@/router"
import axios from "axios"
import drf from '@/api/drf'
export default {

  state: {
    token: localStorage.getItem('jwt') || '',
    currentUser: {},
    profile: '',
    genres: [],
    authError: null,
    refresh: localStorage.getItem('refresh') || '',
    selectedGenres: [],
    nowSelectGenrePk : '',
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `JWT ${state.token}`}),
    genres: state => state.genres,
    refresh: state => state.refresh,
    selectedGenres: state => state.selectedGenres,
    nowSelectGenrePk: state => state.nowSelectGenrePk,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_GENRELIST:(state, genres) => state.genres = genres,
    SET_REFRESH: (state, refresh) => state.refresh = refresh,
    SET_SELECTED_GENRES:(state, genres) => state.selectedGenres = genres,
    SET_NOW_GENRE_PK: (state, genrePk) => state.nowSelectGenrePk = genrePk,
  },
  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('jwt', token)
      console.log('토큰 로컬에 저장')
    },

    saveRefresh({commit}, refresh) {
      commit('SET_REFRESH', refresh)
      localStorage.setItem('refresh', refresh)
    },

    removeRefresh({ commit }) {
      commit('SET_REFRESH', '')
      localStorage.setItem('refresh', '')
    },

    removeToken({ commit }) {
      commit('SET_TOKEN', '')
      localStorage.setItem('jwt', '')
    },

    login({ commit,dispatch }, credentials) {
      axios({
      url: drf.accounts.login(),
      method: 'post',
      data: credentials
    })
      .then(res => {
        dispatch('getJwt',credentials)
        dispatch('saveRefresh', res.data.refresh_token)
        commit('SET_CURRENT_USER', res.data.user.pk)
        // router.push({name: 'Main'})
        return res
      })
      .then((res)=>{
        console.log(res.data)
        router.push({name: 'Wating'})
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
      })
    },

    signup({ commit, dispatch }, credentials) {
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          res
          dispatch('getJwt',{email:credentials.email,password:credentials.password1})
          router.push({name: 'CreateProfile'})
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    
    createProfile({commit,getters},credentials){
      axios({
        url: drf.accounts.createProfile(),
        method:'post',
        data: credentials,
        headers: getters.authHeader,
      })
      .then((res)=>{
        console.log(res)
        // const image = 'http://127.0.0.1:8000/'+res.data.image
        // const backdrop =  'http://127.0.0.1:8000/'+res.data.backdrop
        // const nickname = res.data.nickname
        // const birth = res.data.birth
        // const introduce = res.data.introduce
        // const gender = res.data.gender
        // const location1 = res.data.location1
        // const location2 = res.data.location2
        router.push({name:'SelectGenre'})
      })
      .catch(err => {
        console.error(err.response.data)
        commit('SET_AUTH_ERROR',err.response.data)
      })
    },

    logout({ getters, dispatch, commit }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        data: {refresh: getters.refresh},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          alert('성공적으로 logout!')
          commit('SET_REFRESH', '')
          dispatch('removeRefresh')
          router.push({ name: 'login' })
        })
        .catch(err => {
          console.error(err.response)
        })
        .finally(
          console.log(getters.refresh)
        )
    },

    getJwt({dispatch },credentials) {
      axios({
        url: drf.accounts.getJwtToken(),
        method: 'post',
        data: credentials,
      })
        .then(res => {
          console.log('jwt에서 토큰 받기 !')
          const token = res.data.token
          console.log(token)
          dispatch('saveToken', token)
        })
        .catch(err => {
          if (err.response.status === 401) {
            dispatch('removeToken')
            router.push({ name: 'login' })
          }
        })
    },


    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER',res.data)

          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, user_pk) {
      axios({
        url: drf.accounts.profile(user_pk),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        console.log(res.data,'success')
        commit('SET_PROFILE', res.data)
        
      })
    },

    loadGenre({getters, commit}){
      axios({
        url: drf.accounts.genrelist(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_GENRELIST', res.data)
      })
    },

    selectGenre({getters, commit}, genre){
      axios({
        url: drf.accounts.selectGenre(genre),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_SELECTED_GENRES', res.data.like_genres)
      })

    },
  },
}

