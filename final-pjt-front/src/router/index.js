import Vue from 'vue'
import VueRouter from 'vue-router'
import UserView from '@/views/UserView.vue'
import SearchView from '@/views/SearchView.vue'
import MainView from '@/views/MainView.vue'
import CrewView from '@/views/CrewView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import CastDetailView from '@/views/CastDetailView.vue'
import CrewDetailView from '@/views/CrewDetailView.vue'
import CrewCreateView from '@/views/CrewCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/movie',
    name: 'Main',
    component: MainView
  },
  {
    path: '/user',
    name: 'User',
    component: UserView
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
    path: '/castdetail',
    name: 'CastDetail',
    component: CastDetailView
  },
  {
    path: '/moviedetail',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/crewdetail',
    name: 'CrewDetail',
    component: CrewDetailView
  },
  {
    path: '/crewcreate',
    name: 'CrewCreate',
    component: CrewCreateView
  },
  {
    path: '/articledetail',
    name: 'ArticleDetail',
    component: ArticleDetailView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
