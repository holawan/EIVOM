<template>
  <div>
    <h1>MyMovieList</h1>
    <movie-list-item
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'


export default {
  name:'MyMovieList',
  components:{
    MovieListItem
  },
  props:{ movies:Array },
  computed:{

  },
}
</script>

<style>

</style>