<template>
  <div>
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
  name:'MovieList',
  components:{MovieListItem},
  props:{
    movies:Array,
  }
}
</script>

<style>

</style>