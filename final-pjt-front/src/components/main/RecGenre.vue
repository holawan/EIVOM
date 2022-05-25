// 선호장르에 따른 영화 추천
// 선호장르는 가입할 때 3개 이상 선택

<template>
  <div>
    <h1>Rec Genre</h1>

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