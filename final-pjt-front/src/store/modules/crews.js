import drf from "@/api/drf"
import router from "@/router"
import axios from "axios"
import _ from 'lodash'


export default{
  state: {
    token: localStorage.getItem('jwt') || '',
    currentUser: {},
    crews: [],
    crew: {},
    article:{},
    articles:[],
    comment: {},
    comments: [],

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
    comment: state => state.comment,
    comments: state => state.comments,
    isArticle: state => !_.isEmpty(state.article),
    isAuthor: (state, getters) => {
      return state.article.user?.pk === getters.currentUser.pk
    }

  },

  mutations:{
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_CREW: (state, crew) => state.crew = crew,
    SET_CREWS: (state, crews) => state.crews = crews,
    SET_ARTICLE: (state, article) => state.article = article,
    SET_ARTICLES: (state, articles) => state.articles = articles,
    SET_COMMENT: (state, comment) => state.comment = comment,
    SET_COMMENTS: (state, comments) => state.comments = comments,

  },

  actions:{
    
    createCrew({getters,dispatch}, credentials){
      axios({
        url: drf.crews.create(),
        method: 'post',
        data: credentials,
        headers: getters.authHeader1,
      })
      .then(res => {
        router.push({name:'CrewDetail', params:{crew_pk: res.data.id}})
        dispatch('joinCrew',res.data.id)
      })
    },

    joinCrew({commit, getters}, crew_pk){
      axios({
        url:drf.crews.crew(crew_pk),
        method: 'post',
        headers: getters.authHeader1,
      })
      .then(res => commit('SET_CREW', res.data))
      .catch(err => console.error(err.response))
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

    fetchCrews({commit, getters}){
      axios({
        url: drf.crews.crews(),
        method:'get',
        headers: getters.authHeader1,
      })
      .then(res => {
        commit ('SET_CREWS', res.data)
        console.log(res.data)
      })
      .catch(err => console.error(err.response))
    },

    createArticle({getters, commit}, {crew_pk, article}){
      axios({
        url: drf.crews.articles(crew_pk),
        method: 'post',
        data: article,
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({ name:'ArticleDetail', params:{crew_pk:crew_pk, article_pk:getters.article.pk} ,query: { timestamp: Date.now() } })
      })
    },

    updateArticle({commit, getters}, {crew_pk, article_pk, title, content}){
      axios({
        url: drf.crews.article(crew_pk, article_pk),
        method: 'put',
        data: {title, content},
        headers:getters.authHeader1,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        router.push({name: 'ArticleDetail', params:{crew_pk:crew_pk, article_pk:getters.article.pk, query: { timestamp: Date.now() }}})
      })
    },

    deleteArticle({commit, getters}, {crew_pk, article_pk}){
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url:drf.crews.article(crew_pk, article_pk),
          method: 'delete',
          headers: getters.authHeader1,
        })
        .then(()=>{
          commit('SET_ARTICLE', {})
          router.push({name: 'CrewDetail', params:{crew_pk:crew_pk}})
        })
        .catch(err => console.error(err.resoponse))
      }
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
    },

    fetchArticle({commit, getters}, {crew_pk, article_pk}){
      axios({
        url: drf.crews.article(crew_pk, article_pk),
        method: 'get',
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_ARTICLE', res.data)
        console.log(res.data)
      })
      .catch(err => console.error(err.resoponse))
    },

    createComment({commit, getters}, {crew_pk, article_pk, content}){
      const comment= {content}
      axios({
        url: drf.crews.comments(crew_pk, article_pk),
        method: 'post',
        data: comment,
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_COMMENT', res.data)
        router.push({ name:'ArticleDetail', params:{crewId:crew_pk, articleId:article_pk},query: { timestamp: Date.now() }})
      })
      .catch(err => console.error(err.resoponse))
    },

    updateComment({commit, getters}, {crew_pk, article_pk, comment_pk, content}){
      const comment = {content}

      axios({
        url: drf.crews.comment(crew_pk, article_pk, comment_pk),
        method: 'put',
        data: comment,
        headers: getters.authHeader1,
      })
      .then(res => {
        commit('SET_COMMENTS', res.data)
      })
      .catch(err => console.error(err.response))
    },

    deleteComment({commit, getters}, {crew_pk, article_pk, comment_pk}){
     
        axios({
          url: drf.crews.comment(crew_pk, article_pk, comment_pk),
          method: 'delete',
          data: {},
          headers: getters.authHeader1,
        })
        .then(res => {
          commit('SET_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    fetchComments({commit, getters}, {crew_pk, article_pk} ){
      axios({
        url: drf.crews.comments(crew_pk, article_pk),
        method: 'get',
        headers: getters.authHeader1,
      })
      .then(res => {
        console.log('했냐?')
        commit('SET_COMMENTS', res.data)
      })
      .catch(err => console.error(err.response))
    }
  },
}
