// 현재 상영중인 영화 캐러샐로 보여주기

<template>
  <div>
    <div style="background-color:white; height:200px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">BoxOffice</h1>
    </div>
    <!-- movies -->
    <movie-list
      :movies="nowPlayingMovies"
    ></movie-list>
    <hr>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default {
  name: 'BoxOffice',
  components:{
    MovieList
  }, 
  computed:{
    ...mapGetters(['nowPlayingMovies'])
  },
  methods:{
    ...mapActions(['getNowPlaying'])
  },
  mounted(){
    this.getNowPlaying()
  },

}
</script>

<style>

</style>