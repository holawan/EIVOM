// 현재 상영중인 영화 캐러샐로 보여주기

<template>
  <div>
    <head>
      <h1>BoxOffice</h1>
    </head>

    <movie-list-item
      v-for="movie in nowPlayingMovies"
      :key="movie.pk"
      :movie="movie"
    ></movie-list-item>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'

export default {
  name: 'BoxOffice',
  components: {
    MovieListItem,
  },
  computed:{
    ...mapGetters(['nowPlayingMovies'])
  },
  methods:{
    ...mapActions(['getNowPlaying'])
  },
  created(){
    this.nowPlayingMovies()
  }
}
</script>

<style>

</style>