<template>
  <div>
    <h1>MovieDetailView</h1>
    <h2>MovieInfo</h2>
    <movie-cast></movie-cast>
    <movie-review></movie-review>
    <movie-rec-similar></movie-rec-similar>
  </div>
</template>

<script>
import MovieCast from '@/components/MovieCast.vue'
import MovieReview from '@/components/MovieReview.vue'
import MovieRecSimilar from '@/components/MovieRecSimilar.vue'


export default {
  name: 'MovieDetailView',
  components:{
    MovieCast,
    MovieReview,
    MovieRecSimilar,

  }
}
</script>

<style>

</style>