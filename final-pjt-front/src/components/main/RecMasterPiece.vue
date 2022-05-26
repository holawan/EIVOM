// tmdb 기반 명작추천 // get top rated movie

<template>
  <div>
    <div style="background-color:white; height:50px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">TMDB 추천 명작</h1>

    </div>

    <!-- movies -->
    <movie-list
      :movies="topRatedMovies"
    ></movie-list>
    <hr>
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