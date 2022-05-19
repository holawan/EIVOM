<template>
  <div>
    <h1>CrewMovielist</h1>
    <movie-list-item></movie-list-item>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
  name:'CrewMovieList',
  components:{
    MovieListItem,
  }
}
</script>

<style>

</style>