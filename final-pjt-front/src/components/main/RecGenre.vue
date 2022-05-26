// 선호장르에 따른 영화 추천
// 선호장르는 가입할 때 3개 이상 선택

<template>
  <div>
    <div style="background-color:white; height:50px"></div>
    <div class="mx-5">
      <h1 align="start" style="font-family: 'East Sea Dokdo', cursive; font-size:100px">당신의 취향을 저격할 영화 </h1>
      <h1 align="start">회원님이 선택한 장르를 기반으로 추천됩니다 :)</h1>
    </div>

    <movie-list
      :movies="recGenreMovies"
    ></movie-list>

  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieList from '../MovieList.vue'

export default {
  name: 'RecGenre',
  components:{
    MovieList,
  },
  methods:{
    ...mapActions(['getGenreRecMovies',])
  },
  computed:{
    ...mapGetters(['authHeader', 'recGenreMovies'])
  },
    mounted(){
    if(this.recGenreMovies.length) {
      console.log('있어!')
      console.log(this.recGenreMovies)
      }else{
        console.log('없어!받아올게')
        this.getGenreRecMovies(this.authHeader)
      }

  },
}
</script>

<style>

</style>