<template>
  <div>
    <h1>CrewDetailView</h1>
    <h2>CrewInfo</h2>
    <crew-movie-list></crew-movie-list>
    <article-list></article-list>
  </div>
</template>

<script>
import CrewMovieList from '@/components/CrewMovieList.vue'
import ArticleList from '@/components/ArticleList.vue'

export default {
  name:'CrewDetailView',
  components:{
    CrewMovieList,
    ArticleList,
  }

}
</script>

<style>

</style>