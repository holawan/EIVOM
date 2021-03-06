import Vue from 'vue'
import VueRouter from 'vue-router'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'
import MainView from '@/views/MainView.vue'
import CrewView from '@/views/CrewView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CastDetailView from '@/views/CastDetailView.vue'
import CrewDetailView from '@/views/CrewDetailView.vue'
import CrewCreateView from '@/views/CrewCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import CreateProfile from '@/views/accounts/CreateProfile.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import SelectGenre from '@/views/accounts/SelectGenre.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'

import WatingView from '@/views/WatingView.vue'
import IntroView from '@/views/IntroView'
import NoneMovieFromMain from'@/views/NoneMovieFromMain.vue'
// import store from '@/store'
Vue.use(VueRouter)

// const requireAuth = () => (to,from,next) =>{
//   if (store.accounts.state.token !== '') {
//     return next('/login');
//   }
//   next();
// }

const routes = [
  {
    path:'/',
    name:'Intro',
    component: IntroView,
  },
  {
    path:'/wating',
    name:'Wating',
    component: WatingView,
  },
  {
    path:'/sorry',
    name:'Sorry',
    component: NoneMovieFromMain,
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/create_profile',
    name: 'CreateProfile',
    component: CreateProfile
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/selectgenre',
    name: 'SelectGenre',
    component: SelectGenre
  },
  {
    path: '/movie',
    name: 'Main',

    component: MainView,
    // beforeEnter : requireAuth

  },
  {
    path: '/profile/:user_pk',
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/crew',
    name: 'Crew',
    component: CrewView
  },
  {
    path: '/castdetail/:castId',
    name: 'CastDetail',
    component: CastDetailView
  },
  {
    path: '/moviedetail/:movie_pk',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/crewdetail/:crew_pk',
    name: 'CrewDetail',
    component: CrewDetailView
  },
  {
    path: '/crewcreate',
    name: 'CrewCreate',
    component: CrewCreateView
  },
  {
    path: '/:crew_pk/articlecreate',
    name: 'ArticleCreate',
    component: ArticleCreateView
  },
  {
    path: '/:crew_pk/articleedit/:article_pk',
    name: 'ArticleEdit',
    component: ArticleEditView
  },
  {
    path: '/:crew_pk/articles/:article_pk',
    name: 'ArticleDetail',
    component: ArticleDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



// router.beforeEach((to, from, next) => {
//   // 이전 페이지에서 발생한 에러메시지 삭제
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup']

//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('Require Login. Redirecting..')
//     next({ name: 'Login' })
//   } else {
//     next()
//   }

//   if (!isAuthRequired && isLoggedIn) {
//     next({ name: 'Main' })
//   }
// })

// /*
// Navigation Guard 설정
//   (이전 페이지에서 있던 에러 메시지 삭제)

//   로그인(Authentication)이 필요 없는 route 이름들 저장(/login, /signup)

//   0. router 에서 이동 감지

//   1. 현재 이동하고자 하는 페이지가 로그인이 필요한지 확인
  
//   2. 로그인이 필요한 페이지인데 로그인이 되어있지 않다면
//     로그인 페이지(/login)로 이동

//   3. 로그인이 되어 있다면
//     원래 이동할 곳으로 이동
  
//   4. 로그인이 되어있는데 /login, /signup 페이지로 이동한다면
//     메인 페이지(/)로 이동
    

// */

export default router
