import router from "@/router"
import axios from "axios"
import drf from '@/api/drf'

export default {

  state: {
    token: localStorage.getItem('jwt') || '',
    currentUser: {},
    profile: {},
    genres: [],
    authError: null,
    
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `JWT ${state.token}`}),
    genres: state => state.genres,
  },
  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SET_GENRELIST: (state, genres) => state.genres = genres,
  },
  actions: {
    saveToken({ commit }, token) {
      commit('SET_TOKEN', token)
      localStorage.setItem('jwt', token)
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
          const token = res.data.token
          dispatch('saveToken', token)
          // dispatch('fetchCurrentUser')
          console.log(token)
          console.log(res)
          router.push({name: 'CreateProfile'})
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
          console.log(res)
          const token = res.data.token
          dispatch('saveToken', token)
          const credential = {
            'email' : credentials.email,
            'password' : credentials.password1
          }
          dispatch('login',credential)
          console.log('login!!!')
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

      }
        
      )
      .catch(err => {
        console.log(credentials)
        console.error(err.response)
        commit('SET_AUTH_ERROR',err.response.data)
      }
      )

    },

    logout({ getters, dispatch }) {
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          alert('성공적으로 logout!')
          router.push({ name: 'login' })
        })
        .error(err => {
          console.error(err.response)
        })
    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      if (getters.isLoggedIn) {
        axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => commit('SET_CURRENT_USER', res.data))
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    fetchProfile({ commit, getters }, { username }) {
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
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
        console.log(res.data)
        commit('SET_GENRELIST', res.date)
      })
    },
  },

}
