// 현재 상영중인 영화 캐러샐로 보여주기

<template>
  <div>
    <head>
      <h1>BoxOffice</h1>
    </head>

    <movie-list
      :movies="nowPlayingMovies.slice(0, 6)"
    ></movie-list>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default {
  name: 'BoxOffice',
  components: {
    MovieList,
  },
  computed:{
    ...mapGetters(['nowPlayingMovies'])
  },
  methods:{
    ...mapActions(['getNowPlaying'])
  },
  created(){
    this.getNowPlaying()
  }
}
</script>

<style>

</style>