<template>
  <div>
    <h1>CrewMovielist</h1>
    <movie-list-item
      v-for="movie in crewMovies"
      :key="movie.movieid"
      :movie-item="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import MovieListItem from './MovieListItem.vue'

export default {
  name:'CrewMovieList',
  components:{
    MovieListItem,
  },
  computed: {
    ...mapGetters(['crewMovies'])
  }
}
</script>

<style>

</style>