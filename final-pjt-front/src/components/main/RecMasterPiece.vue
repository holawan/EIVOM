// tmdb 기반 명작추천 // get top rated movie

<template>
  <div>
    <h1>
      RecMasterPiece
    </h1>

    <!-- movies -->
    <div
      v-for="movie in topRatedMovies"
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
  name: 'RecMasterPiece',
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