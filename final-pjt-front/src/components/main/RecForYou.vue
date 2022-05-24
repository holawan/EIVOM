// 당신을 위한 추천
// 클러스터링 / ML

<template>
  <div class="home container">
    <div>
      <h1 class="d-flex justify-content-center">RecForYou</h1>
    </div>
    <div class="d-flex justify-content-center">
      <h2>{{ cmTitle }}</h2>
    </div>
    
    <div class="row justify-content-center">
      <movie-list-item
        v-for="movie in this.clusterMovies"
        :key="movie.pk"
        :movie="movie"
      ></movie-list-item>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'

export default {
  name: 'RecForYou',
  components:{
    MovieListItem
  },
  methods:{
    ...mapActions(['getClusterMovies']),
  },
  computed:{
    ...mapGetters(['clusterMovies', 'cmTitle','authHeader'])
  },
  created(){
    this.getClusterMovies(this.authHeader)

  },
    
}

</script>

<style>

.home{
  display: flex;

}

</style>