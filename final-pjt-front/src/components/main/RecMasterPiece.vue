// tmdb 기반 명작추천 // get top rated movie

<template>
  <div>
    <h1>
      RecMasterPiece
    </h1>

    <!-- movies -->
    <movie-list
      :movies="topRatedMovies"
    ></movie-list>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default {
  name: 'RecMasterPiece',
  components:{
    MovieList
  }, 
  computed:{
    ...mapGetters(['topRatedMovies'])
  },
  methods:{
    ...mapActions(['getTopRatedMovie'])
  },
  mounted(){
    this.getTopRatedMovie()
  },
}
</script>

<style>

</style>