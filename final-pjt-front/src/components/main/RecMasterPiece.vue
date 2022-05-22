// tmdb 기반 명작추천 // get top rated movie

<template>
  <div>
    <h1>
      RecMasterPiece
    </h1>
    <movie-list-item
      v-for="movie in topRatedMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'

export default {
  name: 'RecMasterPiece',
  components:{
    MovieListItem,
  },
  computed:{
    ...mapGetters(['topRatedMovies'])
  },
  methods:{
    ...mapActions(['getTopRatedMovie'])
  },
  created(){
    this.getTopRatedMovie()
  },
}
</script>

<style>

</style>