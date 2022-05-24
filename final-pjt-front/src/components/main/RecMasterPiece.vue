// tmdb 기반 명작추천 // get top rated movie

<template>
  <div>
    <h1>
      RecMasterPiece
    </h1>
    <div class="box">
      <!-- <div class="row flex-row flex-nowrap">
          <movie-list-item
            v-for="movie in topRatedMovies"
            :key="movie.id"
            :movie="movie"
          ></movie-list-item>
          
      </div> -->

      <div class="tab">
          <movie-list-item
            v-for="movie in topRatedMovies"
            :key="movie.id"
            :movie="movie"
          ></movie-list-item>
          
      </div>
    </div>
    
    
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
.box{max-width:960px; width:100%; height:800px; border:1px solid #ccc; margin:0 auto;}
#tab movie-list-item{white-space:nowrap; 
    overflow-x: auto; text-align:center}
</style>