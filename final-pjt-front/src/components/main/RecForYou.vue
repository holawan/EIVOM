// 당신을 위한 추천
// 클러스터링 / ML

<template>
  <div>
    <div style="background-color:white; height:50px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">이런 영화 어때요?</h1>
      <h1 align="start">{{ cmTitle }} !</h1>
    </div>

      <movie-list
        :movies="clusterMovies"
      ></movie-list>
      <hr>
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