// 사람들이 많이 조회한 영화 추천

<template>
  <div>
    <h1>Rec Highly View Movie</h1>
    
    <movie-list
      :movies="recViewCountsMovies"
    ></movie-list>

  </div>
</template>

<script>
import MovieList from '../MovieList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RecHighlyView',
  components:{
    MovieList,
  },
  methods:{
    ...mapActions(['getViewCountMovies',])
  },
  computed:{
    ...mapGetters(['authHeader', 'recViewCountsMovies'])
  },
  mounted(){
    if(this.recViewCountsMovies.length) {
      console.log('있어!')
      console.log(this.recViewCountsMovies)
      }else{
        console.log('없어!받아올게')
       this.getViewCountMovies(this.authHeader)
      }

  },
}
</script>

<style>

</style>