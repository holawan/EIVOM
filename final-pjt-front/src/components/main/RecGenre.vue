// 선호장르에 따른 영화 추천
// 선호장르는 가입할 때 3개 이상 선택

<template>
  <div>
    <h1>Rec Genre</h1>
    <movie-list-item
      v-for="movie in recGenreMovies"
      :key="movie.id"
      :movie="movie"
    ></movie-list-item> 
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieListItem from '../MovieListItem.vue'

export default {
  name: 'RecGenre',
  components:{
    MovieListItem,
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