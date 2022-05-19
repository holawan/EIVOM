<template>
  <div>
    <h1>MyMovieList</h1>
    <movie-list-item></movie-list-item>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'


export default {
  name:'MyMovieList',
  components:{
    MovieListItem
  }
}
</script>

<style>

</style>