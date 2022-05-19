<template>
  <div>
    <h1>MovieCast</h1>
    <movie-cast-item></movie-cast-item>
  </div>
</template>

<script>
import MovieCastItem from './MovieCastItem.vue'

export default {
  name:'MovieCast',
  components:{
    MovieCastItem,
  }

}
</script>

<style>

</style>