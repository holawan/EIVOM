// 현재 상영중인 영화 캐러샐로 보여주기

<template>
  <div>
    <head>
      <h1>BoxOffice</h1>
    </head>

    <!-- movies -->
    <div
      v-for="movie in nowPlayingMovies"
      :key="movie.id"
      :movie="movie"
    >
      <div>
        <router-link :to="{name: 'MovieDetail', params: { movie_pk : movie.id} }">
          <div class="card card-block pr-3" style="width: 18rem;">
            <img :src="'https://image.tmdb.org/t/p/w400/'+ movie.poster_path" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text">{{ movie.title }}</p>
            </div>
          </div>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'BoxOffice',

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