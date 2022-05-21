import Vue from 'vue'
import Vuex from 'vuex'

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
