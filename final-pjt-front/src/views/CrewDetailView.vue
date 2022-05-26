<template>
  <div>
    <nav-bar :now="'CrewDetail'"></nav-bar>

    <!-- crew info -->
    <div>
      <img :src="`http://127.0.0.1:8000${crew.crew_image}`" alt="">
      {{crew}}
      {{ crew.crewname }}
      <p> {{ crew.crew_location1 }}</p>
      {{ crew.crewintro }}
    </div>

    <!-- article 만들기 -->
    <div>
       <router-link :to="{ name: 'ArticleCreate', params:{ crew_pk: crew_pk } }">
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
      :crew_pk="crew_pk"
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
      crew_pk: this.$route.params.crew_pk
    }
  },
  computed:{
    ...mapGetters(['crew', 'isLeader', 'articles'])
  },
  methods:{
    ...mapActions(['fetchCrew', 'fetchProfile', 'fetchArticles'])
  },
  created(){
    this.fetchCrew(this.crew_pk)
    this.fetchArticles(this.crew_pk)
    console.log(this.crew_pk)
  }

}
</script>

<style>

</style>