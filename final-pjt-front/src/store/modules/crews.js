import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"


export default{
  state: {
    token: localStorage.getItem('jwt') || '',
    currentUser: {},
    crews: [],
    crew: {},
    article:{},
    articles:[],

  },

  getters:{
    // isResisterdIn: {},
    isLoggedIn1: state => !!state.token,
    currentUser1: state => state.currentUser,
    crews: state => state.crews,
    crew: state => state.crew,
    isLeader: (state, getters) => {
      return state.crew.crew_leader?.email === getters.currentUser.email
    },
    authHeader1: state => ({ Authorization: `JWT ${state.token}`}),
    article: state=> state.article,
    articles: state => state.articles,

  },

  mutations:{
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_CREW: (state, crew) => state.crew = crew,
    SET_CREWS: (state, crews) => state.crews = crews,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLES: (state, articles) => state.articles = articles,

  },

  actions:{
    
    createCrew({getters}, credentials){
      axios({
        url: drf.crews.create(),
        method: 'post',
        data: credentials,
        headers: getters.authHeader1,
      })
      .then(res => {
        console.log(res)
        router.push({name:'CrewDetail', params:{crewId: res.data.id}})
      })
      .finally(()=>{
        console.log(credentials)
      })
    },

    fetchCrew({commit, getters}, crewId){
      axios({
        url: drf.crews.crew(crewId),
        method: 'get',
        headers: getters.authHeader1
      })
      .then(res => {
        commit('SET_CREW', res.data)
      })
      .catch(err => {
        console.error(err.response)
      })
    },

    createArticle({getters, commit}, payload){
      axios({
        url: drf.crews.articles(payload.crewId),
        method: 'post',
        data: payload.article,
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({ name:'ArticleDetail', params:{article_pk:getters.article.pk}})
      })
    },

    fetchArticles({commit, getters}, crewId){
      axios({
        url:drf.crews.articles(crewId),
        method: 'get',
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_ARTICLES', res.data)
      })
      .catch(err => console.error(err.resoponse))
    }

  },
}
