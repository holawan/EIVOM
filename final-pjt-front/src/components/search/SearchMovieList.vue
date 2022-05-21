<template>
  <div>
    <h1>SearchList</h1>
    <movie-list-item
      v-for="movie in searchMovies"
      :key="movie.movieid"
      :movie-item="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'

export default {
  name:'SearchList',
  components:{
    MovieListItem,
  },
  computed:{
    ...mapGetters(['searchMovies'])
  }

}
</script>

<style>

</style>