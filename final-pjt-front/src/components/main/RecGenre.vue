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
  created(){
    this.getGenreRecMovies(this.authHeader)
  }

}
</script>

<style>

</style>