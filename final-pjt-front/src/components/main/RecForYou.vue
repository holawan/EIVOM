// 당신을 위한 추천
// 클러스터링 / ML

<template>
  <div>
    <div>
      <h1>RecForYou</h1><br><hr>
      <h2>{{ cmTitle }}</h2><hr>
    </div>

      <movie-list
        :movies="clusterMovies"
      ></movie-list>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default {
  name: 'RecForYou',
  components:{
    MovieList
  },
  methods:{
    ...mapActions(['getClusterMovies','removeMovietest']),
  },
  computed:{
    ...mapGetters(['clusterMovies', 'cmTitle','authHeader'])
    
  },
  mounted(){
    if(this.clusterMovies.length) {
      console.log('있어!')
      console.log(this.clusterMovies)
      }else{
        console.log('없어!받아올게')
        this.getClusterMovies(this.authHeader)
      }

  },
}

</script>

<style>

</style>