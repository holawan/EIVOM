// 사람들이 많이 조회한 영화 추천

<template>
  <div>
    <div style="background-color:white; height:50px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">최근 조회수가 높은 영화</h1>
    </div>
    <movie-list
      :movies="recViewCountsMovies"
    ></movie-list>
  <hr>
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