<template>
  <div>
    <h1>SearchView</h1>
    <search-var></search-var>
    <search-genre></search-genre>
    <search-movie-list></search-movie-list>
  </div> 
</template>

<script>
import SearchVar from '@/components/search/SearchVar.vue'
import SearchMovieList from '@/components/search/SearchMovieList.vue'
import SearchGenre from '@/components/search/SearchGenre.vue'

export default {
  name: 'SearchView',
  components: {
    SearchVar,
    SearchMovieList,
    SearchGenre,
  }
  

}
</script>

<style>

</style>