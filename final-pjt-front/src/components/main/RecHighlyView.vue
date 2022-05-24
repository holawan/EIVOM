// 사람들이 많이 조회한 영화 추천

<template>
  <div>
    <h1>Rec Highly View Movie</h1>

    <movie-list-item
      v-for="movie in recViewCountsMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import MovieListItem from '../MovieListItem.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecHighlyView',
  components:{
    MovieListItem,
  },
  methods:{
    ...mapActions(['getViewCountMovies',])
  },
  computed:{
    ...mapGetters(['authHeader', 'recViewCountsMovies'])
  },
  created(){
    this.getViewCountMovies(this.authHeader)
  }
}
</script>

<style>

</style>