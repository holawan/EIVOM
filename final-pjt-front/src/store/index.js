import Vue from 'vue'
import Vuex from 'vuex'
import axiox from 'axios'
import router from '@/router'

Vue.use(Vuex)
import accounts from './modules/accounts'
import movies from './modules/movies'
import crews from './modules/crews'


export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    modules: { accounts, movies, crews },
  }
})
