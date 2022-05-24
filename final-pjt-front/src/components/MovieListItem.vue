<template>
  <div>
    <router-link :to="{name: 'MovieDetail', params: {movie_pk:movie.pk} }">
      <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" alt="">
      <h3>{{ movie.title }}</h3>
    </router-link>

  </div>
</template>

<script>


export default {
  name: 'MovieListItem',
  props:{
    movie:{
      type:Object
    }
  },

}
</script>

<style>

</style>