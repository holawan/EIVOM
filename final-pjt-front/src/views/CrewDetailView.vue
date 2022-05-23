<template>
  <div>

    <!-- crew info -->
    <div>
      <img :src="`http://127.0.0.1:8000${crew.crew_image}`" alt="">
      {{ crew.crewname }}
      <p> {{ crew.crew_location1 }}  {{ crew.crew_location2 }} </p>
      {{ crew.crew_leader.profile.nickname }}
      {{ crew.crewintro }}
    </div>

    <!-- CREW MOVIE LIST -->
    <movie-list-item
      v-for="movie in crew.movies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
    <article-list
    
    ></article-list>
  </div>
</template>

<script>

import ArticleList from '@/components/ArticleList.vue'
import MovieListItem from '@/components/MovieListItem.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name:'CrewDetailView',
  components:{
    ArticleList,
    MovieListItem,
  },
  data(){
    return{
      crewId: this.$route.params.crewId
    }
  },
  computed:{
    ...mapGetters(['crew', 'isLeader'])
  },
  methods:{
    ...mapActions(['fetchCrew', 'fetchProfile'])
  },
  created(){
    this.fetchCrew(this.crewId)
  }

}
</script>

<style>

</style>