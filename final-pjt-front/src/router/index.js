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


Vue.use(VueRouter)

const routes = [
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
    component: MainView
  },
  {
    path: '/profile/:nickname',
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
    path: '/moviedetail/:movieId',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/crewdetail/:crewId',
    name: 'CrewDetail',
    component: CrewDetailView
  },
  {
    path: '/crewcreate',
    name: 'CrewCreate',
    component: CrewCreateView
  },
  {
    path: '/articledetail/:articlePk',
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

export default router
