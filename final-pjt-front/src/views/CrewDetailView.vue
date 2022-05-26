<template>
  <div>
    <nav-bar :now="CrewDetail"></nav-bar>

    <!-- crew info -->
    <div>
      <img :src="`http://127.0.0.1:8000${crew.crew_image}`" alt="">
      {{ crew.crewname }}
      <p> {{ crew.crew_location1 }}  {{ crew.crew_location2 }} </p>
      {{ crew.crew_leader.profile.nickname }} <br>
      {{ crew.crewintro }}
    </div>

    <!-- article 만들기 -->
    <div>
       <router-link :to="{ name: 'ArticleCreate', params:{ crewId:crew.id } }">
         <button>new Article</button>
        </router-link>
    </div>

    <!-- CREW MOVIE LIST -->
    <movie-list-item
      v-for="movie in crew.movies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>

    <!-- article list -->
    <article-list-item
      v-for="article in articles"
      :key="article.pk"
      :article="article"
    ></article-list-item>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ArticleListItem from '@/components/ArticleListItem.vue'
import MovieListItem from '@/components/MovieListItem.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CrewDetailView',
  components:{
    NavBar,
    ArticleListItem,
    MovieListItem,
  },
  data(){
    return{
      crewId: this.$route.params.crewId
    }
  },
  computed:{
    ...mapGetters(['crew', 'isLeader', 'articles'])
  },
  methods:{
    ...mapActions(['fetchCrew', 'fetchProfile', 'fetchArticles'])
  },
  created(){
    this.fetchCrew(this.crewId)
    this.fetchArticles(this.crewId)
  }

}
</script>

<style>

</style>